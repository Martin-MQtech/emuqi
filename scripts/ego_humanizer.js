/**
 * ego_humanizer.js - ego-browser 人类行为模拟与反风控底层工具库
 *
 * 核心设计目标：
 * 1. 规避各大平台（TikTok, LinkedIn, X, Facebook, Reddit, 微博, 知乎等）行为生物特征识别与机器人风控。
 * 2. 模拟真实人类的物理动力学特征：贝塞尔曲线鼠标轨迹、随机变频按键打字抖动、标点停顿、滚动阻尼、预点击视线停留。
 * 3. 保证现代前端框架（React, Vue, Draft.js, Slate）受控组件的状态持久化（事件链完整触发）。
 */

// 状态追踪：记录当前页面鼠标的最后坐标
const pageMousePositions = new WeakMap();

/**
 * 随机生成 [min, max] 区间内的浮点数或整数
 */
function randomBetween(min, max, integer = false) {
  const val = Math.random() * (max - min) + min;
  return integer ? Math.round(val) : val;
}

/**
 * 带有微小扰动的高斯分布近似延时
 */
async function humanDelay(minMs = 300, maxMs = 800) {
  const ms = randomBetween(minMs, maxMs, true);
  return new Promise((resolve) => setTimeout(resolve, ms));
}

/**
 * 缓动函数：模拟人类肢体加速-匀速-减速的物理运动 (Cubic Ease In-Out)
 */
function easeInOutCubic(t) {
  return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
}

/**
 * 计算三阶贝塞尔曲线点
 */
function getCubicBezierPoint(p0, p1, p2, p3, t) {
  const cx = 3 * (p1.x - p0.x);
  const bx = 3 * (p2.x - p1.x) - cx;
  const ax = p3.x - p0.x - cx - bx;

  const cy = 3 * (p1.y - p0.y);
  const by = 3 * (p2.y - p1.y) - cy;
  const ay = p3.y - p0.y - cy - by;

  const x = ax * Math.pow(t, 3) + bx * Math.pow(t, 2) + cx * t + p0.x;
  const y = ay * Math.pow(t, 3) + by * Math.pow(t, 2) + cy * t + p0.y;
  return { x, y };
}

/**
 * 贝塞尔平滑曲线鼠标轨迹模拟
 * @param {object} page ego-browser page 实例
 * @param {number} targetX 目标 X 坐标
 * @param {number} targetY 目标 Y 坐标
 * @param {object} options 配置参数
 */
async function humanMove(page, targetX, targetY, options = {}) {
  const {
    steps: userSteps,
    jitter = true,
    label = 'human-move'
  } = options;

  let startPos = pageMousePositions.get(page);
  if (!startPos) {
    // 默认起点（视口中央附近偏左）
    startPos = { x: randomBetween(200, 400), y: randomBetween(200, 400) };
  }

  const p0 = { x: startPos.x, y: startPos.y };
  const p3 = { x: targetX, y: targetY };

  const distance = Math.hypot(p3.x - p0.x, p3.y - p0.y);
  if (distance < 5) {
    // 距离极近时直接微移
    await page.mouse.move(targetX, targetY, { label });
    pageMousePositions.set(page, { x: targetX, y: targetY });
    return;
  }

  // 步数根据物理像素距离自适应（每 20~30px 一个步进点，且不少于 12 步，不超过 45 步）
  const steps = userSteps || Math.min(Math.max(Math.round(distance / 22), 14), 45);

  // 随机生成两个偏离直线的控制点 P1 和 P2
  const perpX = -(p3.y - p0.y);
  const perpY = p3.x - p0.x;
  const perpLen = Math.hypot(perpX, perpY) || 1;
  const normPerpX = perpX / perpLen;
  const normPerpY = perpY / perpLen;

  // 弧度偏离系数（距离越长偏离稍大，但在 [-0.25, 0.25] 之间）
  const offset1 = distance * randomBetween(-0.2, 0.2);
  const offset2 = distance * randomBetween(-0.15, 0.15);

  const p1 = {
    x: p0.x + (p3.x - p0.x) * 0.3 + normPerpX * offset1,
    y: p0.y + (p3.y - p0.y) * 0.3 + normPerpY * offset1,
  };
  const p2 = {
    x: p0.x + (p3.x - p0.x) * 0.7 + normPerpX * offset2,
    y: p0.y + (p3.y - p0.y) * 0.7 + normPerpY * offset2,
  };

  for (let i = 1; i <= steps; i++) {
    const rawProgress = i / steps;
    const t = easeInOutCubic(rawProgress);
    let pt = getCubicBezierPoint(p0, p1, p2, p3, t);

    // 人手微震颤 (tremor/jitter)，在接近目标时逐步收敛到 0
    if (jitter && i < steps) {
      const remainingProgress = 1 - rawProgress;
      const noiseLevel = Math.min(1.5 * remainingProgress, 1.2);
      pt.x += randomBetween(-noiseLevel, noiseLevel);
      pt.y += randomBetween(-noiseLevel, noiseLevel);
    }

    await page.mouse.move(Math.round(pt.x), Math.round(pt.y), { label });
    // 步间微小物理运动延时 (6ms ~ 18ms)
    await new Promise((r) => setTimeout(r, randomBetween(6, 18, true)));
  }

  // 确保最终落点精准
  await page.mouse.move(targetX, targetY, { label });
  pageMousePositions.set(page, { x: targetX, y: targetY });
}

/**
 * 悬停于指定元素，带真实视线聚焦延时
 * @param {object} page
 * @param {string} selector CSS选择器
 * @param {object} options
 */
async function humanHover(page, selector, options = {}) {
  const { dwellMin = 150, dwellMax = 380, label = 'human-hover' } = options;

  if (typeof selector === 'string' && selector.startsWith('text=')) {
    const txt = selector.slice(5).replace(/^["']|["']$/g, '');
    await page.waitForFunction((t) => {
      return Array.from(document.querySelectorAll('a, button, span, div, p, input')).some(e => e.innerText?.includes(t));
    }, txt, { timeout: 5000 }).catch(() => {});
  } else {
    await page.waitForSelector(selector, { state: 'visible', timeout: 5000 }).catch(() => {});
  }

  // 获取元素的物理包围盒
  const box = await page.evaluate((sel) => {
    let el = null;
    if (typeof sel === 'string' && sel.startsWith('text=')) {
      const txt = sel.slice(5).replace(/^["']|["']$/g, '');
      el = Array.from(document.querySelectorAll('a, button, span, div, p, input')).find(e => e.innerText?.trim() === txt || e.innerText?.includes(txt));
    } else {
      el = document.querySelector(sel);
    }
    if (!el) return null;
    const r = el.getBoundingClientRect();
    return { x: r.x, y: r.y, width: r.width, height: r.height };
  }, selector);

  if (!box || box.width === 0 || box.height === 0) {
    // 退化到直接 hover
    await page.hover(selector, { label });
    return;
  }

  // 严禁点击绝对几何中心！人类点击通常落在内边距 25% ~ 75% 区域
  const targetX = Math.round(box.x + box.width * randomBetween(0.25, 0.75));
  const targetY = Math.round(box.y + box.height * randomBetween(0.3, 0.7));

  await humanMove(page, targetX, targetY, { label });

  // 聚焦思考延时 (Dwell Time)，模拟眼睛找到目标并准备下压的生理停顿
  await humanDelay(dwellMin, dwellMax);
}

/**
 * 拟人化自然点击（移动 -> 悬停停留 -> 真实按压持握 -> 释放）
 * @param {object} page
 * @param {string} selector
 * @param {object} options
 */
async function humanClick(page, selector, options = {}) {
  const {
    holdMin = 45,
    holdMax = 110,
    postDelayMin = 180,
    postDelayMax = 420,
    label = 'human-click'
  } = options;

  await humanHover(page, selector, { label });

  // 鼠标下压 (Mouse Down)
  await page.mouse.down({ button: 'left' });

  // 真实物理点击按压时长（人类手指接触微动开关的平均时长为 50ms ~ 100ms）
  await humanDelay(holdMin, holdMax);

  // 鼠标释放 (Mouse Up)
  await page.mouse.up({ button: 'left' });

  // 点击后的生理反射延时
  await humanDelay(postDelayMin, postDelayMax);
}

/**
 * 拟人化打字输入（变频击键、标点符号认知停顿、防止被按键频率特征识别）
 * @param {object} page
 * @param {string} selector 输入框选择器
 * @param {string} text 待输入的文本
 * @param {object} options
 */
async function humanType(page, selector, text, options = {}) {
  const {
    clearFirst = false,
    baseKeyDelayMin = 65,
    baseKeyDelayMax = 140,
    label = 'human-type'
  } = options;

  await humanClick(page, selector, { label });

  if (clearFirst) {
    // 模拟全选并删除
    await page.keyboard.press('Meta+A');
    await humanDelay(80, 160);
    await page.keyboard.press('Backspace');
    await humanDelay(120, 250);
  }

  for (let i = 0; i < text.length; i++) {
    const char = text[i];

    // 发送物理按键
    await page.keyboard.type(char);

    // 变频打字抖动（基础按键延时）
    const keyDelay = randomBetween(baseKeyDelayMin, baseKeyDelayMax, true);
    await new Promise((r) => setTimeout(r, keyDelay));

    // 认知停顿 (Cognitive Pause)：遇到标点、空格、换行时暂停更长时间
    if (char === ' ' || char === '，' || char === ',') {
      await humanDelay(160, 320);
    } else if (char === '.' || char === '。' || char === '!' || char === '！' || char === '?' || char === '？' || char === '\n') {
      await humanDelay(350, 750);
    } else if (i % 25 === 0 && i > 0) {
      // 偶发性微小阅读停顿（模拟人类审视打出的文字）
      await humanDelay(200, 500);
    }
  }

  // 确保前端框架双向绑定更新（针对 Vue/React contenteditable）
  await page.evaluate((sel) => {
    const el = document.querySelector(sel);
    if (el) {
      el.dispatchEvent(new Event('input', { bubbles: true }));
      el.dispatchEvent(new Event('change', { bubbles: true }));
    }
  }, selector);

  await humanDelay(200, 450);
}

/**
 * 拟人化长文粘贴与状态同步
 * （当篇幅超过 500 字符时，全字符物理打字耗时过长，采用拟人化快捷键粘贴，但保留人类点击与检查停顿）
 */
async function humanPaste(page, selector, text, options = {}) {
  const { clearFirst = false, label = 'human-paste' } = options;

  await humanClick(page, selector, { label });

  if (clearFirst) {
    await page.keyboard.press('Meta+A');
    await humanDelay(90, 180);
    await page.keyboard.press('Backspace');
    await humanDelay(140, 260);
  }

  // 模拟快捷键粘贴前的心智准备
  await humanDelay(220, 480);

  // 原生安全粘贴
  await page.keyboard.paste(text);

  // 强制派发 input/change 事件以防框架状态未响应
  await page.evaluate((sel) => {
    const el = document.querySelector(sel);
    if (el) {
      el.dispatchEvent(new Event('input', { bubbles: true }));
      el.dispatchEvent(new Event('change', { bubbles: true }));
    }
  }, selector);

  // 模拟粘贴完成后的视觉校验与审查停顿（1~2秒）
  await humanDelay(800, 1600);
}

/**
 * 拟人化平滑微步滚动（带物理惯性阻尼与间歇阅读停顿）
 * @param {object} page
 * @param {number} scrollDeltaY 累计滚动的 Y 轴像素量（正数向下，负数向上）
 * @param {object} options
 */
async function humanScroll(page, scrollDeltaY, options = {}) {
  const {
    stepDeltaMin = 100,
    stepDeltaMax = 220,
    pauseChance = 0.3,
    label = 'human-scroll'
  } = options;

  let remaining = scrollDeltaY;
  const direction = scrollDeltaY >= 0 ? 1 : -1;
  remaining = Math.abs(remaining);

  while (remaining > 0) {
    const currentStep = Math.min(
      remaining,
      randomBetween(stepDeltaMin, stepDeltaMax, true)
    );

    await page.mouse.wheel(0, currentStep * direction, { label });
    remaining -= currentStep;

    // 微步之间的滚轮齿轮延时 (50ms ~ 130ms)
    await humanDelay(50, 130);

    // 随机阅读停顿（模拟用户边滚边看内容）
    if (Math.random() < pauseChance && remaining > 50) {
      await humanDelay(600, 1800);
    }
  }

  // 滚动到达后的平复延时
  await humanDelay(300, 700);
}

/**
 * 平台风控安全冷却门禁
 * 限制同一域名下的高频密集调用，避免触发速率限制 (Rate Limit) 或 IP 行为封禁
 */
const domainCooldownLedger = new Map();

async function safeDomainCooldown(domain, minCooldownSeconds = 5) {
  const now = Date.now();
  const lastTime = domainCooldownLedger.get(domain) || 0;
  const elapsed = (now - lastTime) / 1000;

  if (elapsed < minCooldownSeconds) {
    const waitSeconds = minCooldownSeconds - elapsed;
    console.log(`[SafeGuard] 触发域名 ${domain} 风控防刷保护，安全平滑等待 ${waitSeconds.toFixed(1)} 秒...`);
    await new Promise((r) => setTimeout(r, waitSeconds * 1000));
  }

  domainCooldownLedger.set(domain, Date.now());
}

module.exports = {
  humanDelay,
  humanMove,
  humanHover,
  humanClick,
  humanType,
  humanPaste,
  humanScroll,
  safeDomainCooldown,
  randomBetween,
};
