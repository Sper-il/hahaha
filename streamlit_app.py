import streamlit as st

st.set_page_config(page_title="Tang Bong Hoa", page_icon="🌸", layout="centered")

st.html("""
<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
  <title>Tặng Bông Hoa - Bạn không thể từ chối!</title>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      user-select: none;
    }

    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      overflow: hidden;
      height: 100vh;
      width: 100vw;
      background: #ffe4ec;
    }

    .screen {
      position: fixed;
      inset: 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      transition: opacity 0.6s ease, transform 0.6s ease;
      overflow: hidden;
    }

    .screen.hidden {
      opacity: 0;
      pointer-events: none;
      transform: scale(0.95);
    }

    /* ========== MÀN HÌNH 2: LỜI MỜI (OFFER) ========== */
    .offer-screen {
      background: linear-gradient(160deg, #fff5f7 0%, #ffe4ec 50%, #ffd0e0 100%);
    }

    .offer-container {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 2rem;
      padding: 2rem;
      border-radius: 48px;
      background: rgba(255, 245, 247, 0.5);
      backdrop-filter: blur(4px);
    }

    .offer-avatar {
      width: 90px;
      height: 90px;
      border-radius: 50%;
      background: linear-gradient(135deg, #e94560, #ff8fab);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 2.5rem;
      box-shadow: 0 8px 32px rgba(233,69,96,0.3);
      animation: floatAvatar 3s ease-in-out infinite;
    }

    @keyframes floatAvatar {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-10px); }
    }

    .offer-text {
      text-align: center;
    }

    .offer-greeting {
      font-size: 1rem;
      color: #c0607a;
      margin-bottom: 0.4rem;
      font-weight: 500;
    }

    .offer-main {
      font-size: 1.5rem;
      font-weight: 700;
      color: #2d1a22;
      line-height: 1.4;
      max-width: 340px;
    }

    .offer-main em {
      color: #e94560;
      font-style: normal;
      text-shadow: 0 0 4px #ffb7c5;
    }

    .button-area {
      position: fixed;
      bottom: 80px;
      left: 0;
      right: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 20px;
      pointer-events: none;
      z-index: 20;
    }

    .btn-yes {
      pointer-events: auto;
      border: none;
      padding: 0.9rem 2.2rem;
      border-radius: 60px;
      font-size: 1.1rem;
      font-weight: 700;
      cursor: pointer;
      background: #e94560;
      color: white;
      transition: all 0.2s ease;
      box-shadow: 0 8px 20px rgba(233,69,96,0.4);
      letter-spacing: 0.5px;
      white-space: nowrap;
      z-index: 25;
    }

    .btn-yes:hover {
      background: #d63850;
      transform: translateY(-3px);
      box-shadow: 0 12px 24px rgba(233,69,96,0.5);
    }

    .btn-yes:active {
      transform: translateY(1px);
    }

    .btn-no {
      pointer-events: auto;
      border: 2px solid #ffb7c5;
      padding: 0.9rem 2rem;
      border-radius: 60px;
      font-size: 1rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
      background: rgba(255, 255, 255, 0.95);
      color: #e94560;
      backdrop-filter: blur(4px);
      white-space: nowrap;
      box-shadow: 0 4px 12px rgba(0,0,0,0.05);
      z-index: 25;
    }

    .btn-no:hover {
      background: #fff0f3;
      border-color: #e94560;
      transform: scale(1.02);
    }

    .btn-no--escaping {
      position: fixed !important;
      transition: left 0.2s cubic-bezier(0.2, 0.9, 0.4, 1.1), top 0.2s cubic-bezier(0.2, 0.9, 0.4, 1.1);
      box-shadow: 0 12px 28px rgba(233,69,96,0.3);
      cursor: grab;
      z-index: 1000;
    }

    .btn-no-placeholder {
      display: inline-block;
      visibility: hidden;
      pointer-events: none;
    }

    /* ========== MÀN HÌNH HOA (FLOWER) ========== */
    .flower-screen {
      background: linear-gradient(180deg, #1a0a1e 0%, #2d1035 30%, #3d1545 60%, #1a0a1e 100%);
      overflow: hidden;
    }

    .aurora-layer {
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: 0;
      overflow: hidden;
    }

    .aurora-blob {
      position: absolute;
      border-radius: 50%;
      filter: blur(80px);
      opacity: 0.25;
      animation: auroraFloat 12s ease-in-out infinite;
    }

    .aurora-blob:nth-child(1) {
      width: 60vw; height: 50vh;
      background: radial-gradient(ellipse, #e94560, transparent 70%);
      top: -10%; left: -15%;
      animation-duration: 14s;
      animation-delay: 0s;
    }
    .aurora-blob:nth-child(2) {
      width: 50vw; height: 45vh;
      background: radial-gradient(ellipse, #9b59b6, transparent 70%);
      top: -5%; right: -10%;
      animation-duration: 11s;
      animation-delay: -4s;
      opacity: 0.2;
    }
    .aurora-blob:nth-child(3) {
      width: 55vw; height: 40vh;
      background: radial-gradient(ellipse, #ff6b9d, transparent 70%);
      bottom: 5%; left: 20%;
      animation-duration: 16s;
      animation-delay: -7s;
      opacity: 0.18;
    }
    .aurora-blob:nth-child(4) {
      width: 40vw; height: 35vh;
      background: radial-gradient(ellipse, #c0392b, transparent 70%);
      bottom: -5%; right: -5%;
      animation-duration: 13s;
      animation-delay: -2s;
      opacity: 0.2;
    }

    @keyframes auroraFloat {
      0%, 100% { transform: translate(0, 0) scale(1) rotate(0deg); }
      25% { transform: translate(4vw, 3vh) scale(1.08) rotate(5deg); }
      50% { transform: translate(-3vw, 5vh) scale(0.95) rotate(-3deg); }
      75% { transform: translate(5vw, -2vh) scale(1.05) rotate(4deg); }
    }

    .starfield {
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: 1;
    }

    .star {
      position: absolute;
      border-radius: 50%;
      background: white;
      animation: starTwinkle var(--dur, 3s) ease-in-out infinite;
      animation-delay: var(--delay, 0s);
    }

    @keyframes starTwinkle {
      0%, 100% { opacity: 0.1; transform: scale(0.8); }
      50% { opacity: 1; transform: scale(1.4); }
    }

    .sparkle-layer {
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: 2;
    }

    .sparkle {
      position: absolute;
      width: 4px;
      height: 4px;
      background: radial-gradient(circle, #fff 0%, transparent 70%);
      border-radius: 50%;
      animation: sparkleFloat var(--dur, 6s) ease-in-out infinite;
      animation-delay: var(--delay, 0s);
    }

    .sparkle::before, .sparkle::after {
      content: '';
      position: absolute;
      background: radial-gradient(circle, #fff 0%, transparent 70%);
      border-radius: 50%;
    }
    .sparkle::before {
      width: 8px; height: 2px;
      top: 1px; left: -2px;
    }
    .sparkle::after {
      width: 2px; height: 8px;
      top: -2px; left: 1px;
    }

    @keyframes sparkleFloat {
      0%, 100% { opacity: 0; transform: translateY(0) scale(0) rotate(0deg); }
      15% { opacity: 1; transform: translateY(-10px) scale(1) rotate(45deg); }
      85% { opacity: 1; transform: translateY(-80px) scale(1.2) rotate(90deg); }
      100% { opacity: 0; transform: translateY(-100px) scale(0) rotate(120deg); }
    }

    .bg-deco {
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: 0;
    }

    .bg-circle {
      position: absolute;
      border-radius: 50%;
      opacity: 0.12;
    }

    .bg-circle:nth-child(1) { width: 300px; height: 300px; background: radial-gradient(circle, #e94560, transparent); top: -80px; left: -80px; animation: bgFloat1 8s ease-in-out infinite; }
    .bg-circle:nth-child(2) { width: 200px; height: 200px; background: radial-gradient(circle, #ff85a1, transparent); top: 60px; right: -50px; animation: bgFloat2 6s ease-in-out infinite; }
    .bg-circle:nth-child(3) { width: 250px; height: 250px; background: radial-gradient(circle, #9b59b6, transparent); bottom: -60px; left: 10%; animation: bgFloat3 7s ease-in-out infinite; }
    .bg-circle:nth-child(4) { width: 180px; height: 180px; background: radial-gradient(circle, #e91e63, transparent); bottom: 20%; right: -40px; animation: bgFloat1 9s ease-in-out infinite reverse; }
    .bg-circle:nth-child(5) { width: 120px; height: 120px; background: radial-gradient(circle, #ff6b9d, transparent); top: 40%; left: 5%; animation: bgFloat2 5s ease-in-out infinite 2s; }

    @keyframes bgFloat1 { 0%,100% { transform: translate(0,0) scale(1); } 50% { transform: translate(15px, 15px) scale(1.05); } }
    @keyframes bgFloat2 { 0%,100% { transform: translate(0,0) scale(1); } 50% { transform: translate(-10px, 12px) scale(1.08); } }
    @keyframes bgFloat3 { 0%,100% { transform: translate(0,0) scale(1); } 50% { transform: translate(8px, -10px) scale(1.04); } }

    .flower-wrapper {
      position: relative;
      z-index: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 1.5rem;
      animation: flowerReveal 0.9s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
    }

    @keyframes flowerReveal {
      0% { opacity: 0; transform: scale(0.3) translateY(80px); }
      60% { opacity: 1; transform: scale(1.06) translateY(-12px); }
      100% { opacity: 1; transform: scale(1) translateY(0); }
    }

    .flower-glow-ring {
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .flower-glow-ring::before {
      content: '';
      position: absolute;
      width: 360px;
      height: 360px;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(233,69,96,0.15) 0%, rgba(255,107,157,0.08) 60%, transparent 100%);
      animation: ringPulse 3s ease-in-out infinite;
      box-shadow: 0 0 80px rgba(233,69,96,0.2), 0 0 160px rgba(155,89,182,0.1);
    }

    @keyframes ringPulse {
      0%, 100% { transform: scale(1); opacity: 0.8; }
      50% { transform: scale(1.08); opacity: 1; }
    }

    .flower-svg-wrap {
      width: 300px;
      height: 380px;
      animation: flowerRotate 12s linear infinite;
      filter: drop-shadow(0 0 30px rgba(200,40,80,0.25));
    }

    @keyframes flowerRotate {
      0% { transform: rotate(-2deg); }
      50% { transform: rotate(2deg); }
      100% { transform: rotate(-2deg); }
    }

    .flower-svg-wrap svg { width: 100%; height: 100%; }

    .flower-message {
      text-align: center;
      opacity: 0;
      animation: msgAppear 0.7s ease 0.8s forwards;
    }
    .flower-message .line1 { font-size: 1rem; color: #ff9eb5; margin-bottom: 0.5rem; letter-spacing: 0.3px; }
    .flower-message .line2 { font-size: 1.8rem; font-weight: 800; background: linear-gradient(135deg, #ff6b9d, #ffcdd9, #ff85a1); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; line-height: 1.3; }

    @keyframes msgAppear { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }

    .restart-btn {
      opacity: 0;
      animation: msgAppear 0.6s ease 1.8s forwards;
      margin-top: 0.5rem;
      background: rgba(233,69,96,0.15);
      border: 1px solid rgba(233,69,96,0.4);
      color: #ff9eb5;
      padding: 0.6rem 2rem;
      border-radius: 50px;
      font-size: 0.9rem;
      cursor: pointer;
      transition: all 0.3s;
      letter-spacing: 0.3px;
      backdrop-filter: blur(8px);
    }
    .restart-btn:hover { background: rgba(233,69,96,0.3); transform: translateY(-2px); box-shadow: 0 4px 20px rgba(233,69,96,0.3); }

    .petal {
      position: fixed;
      pointer-events: none;
      z-index: 100;
      opacity: 0;
      animation: petalFall linear forwards;
    }
    @keyframes petalFall {
      0% { opacity: 0.9; transform: translateY(0) rotate(0deg) scale(1); }
      80% { opacity: 0.5; }
      100% { opacity: 0; transform: translateY(105vh) rotate(600deg) scale(0.4); }
    }

    .tiny-toast {
      position: fixed;
      bottom: 30px;
      left: 50%;
      transform: translateX(-50%);
      background: #2d1a22e6;
      color: #ffcdd9;
      padding: 8px 20px;
      border-radius: 40px;
      font-size: 0.8rem;
      font-weight: 500;
      backdrop-filter: blur(8px);
      z-index: 9999;
      pointer-events: none;
      animation: fadeToast 1.2s ease forwards;
    }

    @keyframes fadeToast {
      0% { opacity: 0; transform: translateX(-50%) translateY(20px);}
      15% { opacity: 1; transform: translateX(-50%) translateY(0);}
      85% { opacity: 1; transform: translateX(-50%) translateY(0);}
      100% { opacity: 0; transform: translateX(-50%) translateY(-15px); visibility: hidden;}
    }
  </style>
</head>
<body>

<!-- MÀN HÌNH LỜI MỜI (OFFER) -->
<div class="screen offer-screen" id="screenOffer">
  <div class="offer-container">
    <div class="offer-avatar">
      <svg width="50" height="50" viewBox="0 0 24 24" fill="none">
        <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7z" fill="white"/>
        <circle cx="12" cy="9" r="3" fill="#e94560"/>
      </svg>
    </div>
    <div class="offer-text">
      <div class="offer-greeting">Tặng bạn nhè!</div>
      <div class="offer-main">Bạn có muốn nhận không?</div>
    </div>
  </div>

  <div class="button-area" id="buttonArea">
    <button class="btn-yes" id="btnYes"> Có </button>
    <button class="btn-no" id="btnNo"> Không, cảm ơn</button>
  </div>
</div>

<!-- MÀN HÌNH HOA (KHI NHẬN) -->
<div class="screen flower-screen hidden" id="screenFlower">
  <div class="aurora-layer">
    <div class="aurora-blob"></div>
    <div class="aurora-blob"></div>
    <div class="aurora-blob"></div>
    <div class="aurora-blob"></div>
  </div>
  <div class="starfield" id="starfield"></div>
  <div class="sparkle-layer" id="sparkleLayer"></div>
  <div class="bg-deco">
    <div class="bg-circle"></div><div class="bg-circle"></div><div class="bg-circle"></div>
    <div class="bg-circle"></div><div class="bg-circle"></div>
  </div>
  <div class="flower-wrapper">
    <div class="flower-glow-ring">
      <div class="flower-svg-wrap">
        <svg width="100%" viewBox="0 0 690 870" role="img" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="bg2" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="#fef6f0"/><stop offset="100%" stop-color="#fde8d8"/></linearGradient>
            <linearGradient id="gStem2" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="#357a40"/><stop offset="45%" stop-color="#52b060"/><stop offset="100%" stop-color="#357a40"/></linearGradient>
            <linearGradient id="gLeafL2" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#62c472"/><stop offset="100%" stop-color="#2e7838"/></linearGradient>
            <linearGradient id="gLeafR2" x1="100%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="#62c472"/><stop offset="100%" stop-color="#2e7838"/></linearGradient>
            <linearGradient id="gPB2" x1="30%" y1="0%" x2="70%" y2="100%"><stop offset="0%" stop-color="#e8687a"/><stop offset="100%" stop-color="#b82840"/></linearGradient>
            <linearGradient id="gPBL2" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#e06070"/><stop offset="100%" stop-color="#b02038"/></linearGradient>
            <linearGradient id="gPBR2" x1="100%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="#e06070"/><stop offset="100%" stop-color="#b02038"/></linearGradient>
            <linearGradient id="gPFL2" x1="0%" y1="0%" x2="80%" y2="100%"><stop offset="0%" stop-color="#f8a0b0"/><stop offset="55%" stop-color="#ee7088"/><stop offset="100%" stop-color="#c83858"/></linearGradient>
            <linearGradient id="gPFR2" x1="100%" y1="0%" x2="20%" y2="100%"><stop offset="0%" stop-color="#f8a0b0"/><stop offset="55%" stop-color="#ee7088"/><stop offset="100%" stop-color="#c83858"/></linearGradient>
            <linearGradient id="gPFC2" x1="20%" y1="0%" x2="80%" y2="100%"><stop offset="0%" stop-color="#fdd0d8"/><stop offset="40%" stop-color="#f898ac"/><stop offset="100%" stop-color="#d84868"/></linearGradient>
            <radialGradient id="gGround2" cx="50%" cy="40%" r="50%"><stop offset="0%" stop-color="#c8aa78" stop-opacity="0.6"/><stop offset="100%" stop-color="#9e8050" stop-opacity="0"/></radialGradient>
          </defs>
          <rect width="680" height="860" fill="url(#bg2)" rx="16"/>
          <ellipse cx="340" cy="790" rx="160" ry="32" fill="url(#gGround2)"/>
          <path d="M344 788 Q362 650 356 530 Q350 445 342 395" fill="none" stroke="#1e5028" stroke-width="9" stroke-linecap="round" opacity="0.2"/>
          <path d="M340 788 Q356 648 350 528 Q344 443 338 393" fill="none" stroke="url(#gStem2)" stroke-width="12" stroke-linecap="round"/>
          <path d="M343 775 Q356 648 350 528 Q345 450 340 400" fill="none" stroke="#88e098" stroke-width="3" stroke-linecap="round" opacity="0.28"/>
          <path d="M338 640 C 320 630, 280 610, 248 580 C 226 558, 218 530, 232 516 C 246 504, 270 510, 294 528 C 316 544, 334 580, 338 620 Z" fill="url(#gLeafL2)" stroke="#286032" stroke-width="2" stroke-linejoin="round"/>
          <path d="M336 632 Q286 602 258 568 Q240 546 238 524" fill="none" stroke="#90e0a0" stroke-width="1.8" stroke-linecap="round" opacity="0.5"/>
          <circle cx="236" cy="523" r="4" fill="#c8f0d4" opacity="0.7"/>
          <circle cx="235" cy="521" r="1.5" fill="#fff" opacity="0.8"/>
          <path d="M342 610 C 360 600, 400 578, 432 548 C 454 526, 462 498, 448 484 C 434 472, 410 478, 386 496 C 364 512, 346 548, 342 588 Z" fill="url(#gLeafR2)" stroke="#286032" stroke-width="2" stroke-linejoin="round"/>
          <path d="M344 602 Q394 572 422 538 Q440 516 444 492" fill="none" stroke="#90e0a0" stroke-width="1.8" stroke-linecap="round" opacity="0.5"/>
          <circle cx="445" cy="490" r="4" fill="#c8f0d4" opacity="0.7"/>
          <circle cx="444" cy="488" r="1.5" fill="#fff" opacity="0.8"/>
          <path d="M340 400 C 330 388, 308 370, 298 338 C 286 302, 288 258, 298 226 C 306 200, 318 186, 328 192 C 336 197, 339 220, 340 258 C 341 220, 344 197, 352 192 C 362 186, 374 200, 382 226 C 392 258, 394 302, 382 338 C 372 370, 350 388, 340 400 Z" fill="url(#gPB2)" stroke="#982030" stroke-width="1.5" stroke-linejoin="round"/>
          <path d="M340 392 Q326 358 322 318 Q318 278 326 238 Q332 210 340 200" fill="none" stroke="#f0b0b8" stroke-width="2" stroke-linecap="round" opacity="0.4"/>
          <path d="M340 402 C 322 394, 290 374, 272 338 C 254 302, 256 252, 270 214 C 280 188, 296 172, 312 175 C 326 178, 334 200, 338 240 C 339 270, 340 320, 340 360 Z" fill="url(#gPBL2)" stroke="#982030" stroke-width="1.5" stroke-linejoin="round"/>
          <path d="M330 388 Q304 350 296 308 Q289 268 298 228" fill="none" stroke="#f0b0b8" stroke-width="2" stroke-linecap="round" opacity="0.35"/>
          <path d="M340 402 C 358 394, 390 374, 408 338 C 426 302, 424 252, 410 214 C 400 188, 384 172, 368 175 C 354 178, 346 200, 342 240 C 341 270, 340 320, 340 360 Z" fill="url(#gPBR2)" stroke="#982030" stroke-width="1.5" stroke-linejoin="round"/>
          <path d="M350 388 Q376 350 384 308 Q391 268 382 228" fill="none" stroke="#f0b0b8" stroke-width="2" stroke-linecap="round" opacity="0.35"/>
          <path d="M340 404 C 316 396, 278 374, 262 332 C 248 294, 254 240, 272 200 C 284 172, 302 155, 320 160 C 334 164, 339 196, 340 248 Z" fill="url(#gPFL2)" stroke="#b02840" stroke-width="1.5" stroke-linejoin="round"/>
          <path d="M330 392 Q298 356 288 308 Q280 262 292 218 Q302 185 316 170" fill="none" stroke="#ffd8e0" stroke-width="2.5" stroke-linecap="round" opacity="0.55"/>
          <path d="M340 404 C 364 396, 402 374, 418 332 C 432 294, 426 240, 408 200 C 396 172, 378 155, 360 160 C 346 164, 341 196, 340 248 Z" fill="url(#gPFR2)" stroke="#b02840" stroke-width="1.5" stroke-linejoin="round"/>
          <path d="M350 392 Q382 356 392 308 Q400 262 388 218 Q378 185 364 170" fill="none" stroke="#ffd8e0" stroke-width="2.5" stroke-linecap="round" opacity="0.55"/>
          <path d="M340 404 C 318 392, 300 366, 296 330 C 292 294, 300 248, 314 214 C 323 190, 332 175, 340 172 C 348 175, 357 190, 366 214 C 380 248, 388 294, 384 330 C 380 366, 362 392, 340 404 Z" fill="url(#gPFC2)" stroke="#b02840" stroke-width="1.5" stroke-linejoin="round"/>
          <path d="M340 396 Q324 358 321 316 Q318 276 328 234 Q334 206 340 190" fill="none" stroke="#ffe8ee" stroke-width="3" stroke-linecap="round" opacity="0.65"/>
          <ellipse cx="335" cy="215" rx="7" ry="22" fill="#fff" opacity="0.18" transform="rotate(-8,335,215)"/>
        </svg>
      </div>
    </div>
    <div class="flower-message">
      <div class="line2">Luôn rạng rỡ nhé!</div>
    </div>
    <button class="restart-btn" id="restartBtn">Gửi lại bông hoa</button>
  </div>
</div>

<script>
  // ----- DOM Elements -----
  const screenOffer = document.getElementById('screenOffer');
  const screenFlower = document.getElementById('screenFlower');
  const btnYes = document.getElementById('btnYes');
  const btnNo = document.getElementById('btnNo');
  const restartBtn = document.getElementById('restartBtn');
  const buttonArea = document.getElementById('buttonArea');

  // ----- Quản lý trạng thái "né chuột" cho nút Không -----
  let isNoEscaping = false;
  let placeholderSpan = null;
  let originalParent = null;
  let originalNextSibling = null;

  function showGentleMessage(text) {
    const existingToast = document.querySelector('.tiny-toast');
    if(existingToast) existingToast.remove();
    const toast = document.createElement('div');
    toast.className = 'tiny-toast';
    toast.innerText = text;
    document.body.appendChild(toast);
    setTimeout(() => toast.remove(), 1200);
  }

  function getRandomPosition(btnElement) {
    const btnWidth = btnElement.offsetWidth;
    const btnHeight = btnElement.offsetHeight;
    const maxX = window.innerWidth - btnWidth - 20;
    const maxY = window.innerHeight - btnHeight - 20;
    const minX = 15;
    const minY = 15;
    const yesBtn = btnYes;
    const yesRect = yesBtn.getBoundingClientRect();
    let randomLeft, randomTop;
    let safe = false;
    let attempts = 0;
    while (!safe && attempts < 35) {
      randomLeft = Math.floor(Math.random() * (maxX - minX + 1) + minX);
      randomTop = Math.floor(Math.random() * (maxY - minY + 1) + minY);
      const distanceX = Math.abs(randomLeft - yesRect.left);
      const distanceY = Math.abs(randomTop - yesRect.top);
      if (distanceX > 90 || distanceY > 70) {
        safe = true;
      }
      attempts++;
    }
    return { left: randomLeft, top: randomTop };
  }

  function moveNoToRandomPosition() {
    if (!isNoEscaping || !btnNo.classList.contains('btn-no--escaping')) return;
    const { left, top } = getRandomPosition(btnNo);
    btnNo.style.left = left + 'px';
    btnNo.style.top = top + 'px';
  }

  function activateEscapeMode() {
    if (isNoEscaping) return;
    originalParent = btnNo.parentNode;
    const parentNode = originalParent;
    originalNextSibling = btnNo.nextSibling;
    const rect = btnNo.getBoundingClientRect();
    const btnWidth = btnNo.offsetWidth;
    const btnHeight = btnNo.offsetHeight;
    placeholderSpan = document.createElement('div');
    placeholderSpan.className = 'btn-no-placeholder';
    placeholderSpan.style.width = btnWidth + 'px';
    placeholderSpan.style.height = btnHeight + 'px';
    placeholderSpan.style.display = 'inline-block';
    placeholderSpan.style.margin = '0';
    placeholderSpan.style.pointerEvents = 'none';
    if (originalNextSibling) {
      parentNode.insertBefore(placeholderSpan, originalNextSibling);
    } else {
      parentNode.appendChild(placeholderSpan);
    }
    btnNo.remove();
    document.body.appendChild(btnNo);
    btnNo.classList.add('btn-no--escaping');
    btnNo.style.position = 'fixed';
    btnNo.style.left = rect.left + 'px';
    btnNo.style.top = rect.top + 'px';
    btnNo.style.margin = '0';
    btnNo.style.transform = 'none';
    isNoEscaping = true;
    btnNo.onclick = (e) => {
      e.stopPropagation();
      showGentleMessage('🌸 Bạn không thể từ chối món quà đâu! Hãy nhận hoa đi ạ 🌸');
      btnYes.style.animation = 'none';
      btnYes.offsetHeight;
      btnYes.style.animation = 'floatAvatar 0.3s ease';
      setTimeout(() => { btnYes.style.animation = ''; }, 300);
    };
    btnNo.onmouseenter = () => {
      if (isNoEscaping) {
        moveNoToRandomPosition();
      }
    };
    window.addEventListener('resize', () => {
      if (isNoEscaping && btnNo && document.body.contains(btnNo)) {
        const { left, top } = getRandomPosition(btnNo);
        btnNo.style.left = Math.min(left, window.innerWidth - btnNo.offsetWidth - 10) + 'px';
        btnNo.style.top = Math.min(top, window.innerHeight - btnNo.offsetHeight - 10) + 'px';
      }
    });
  }

  function resetNoButton() {
    if (!isNoEscaping) {
      if (placeholderSpan && placeholderSpan.parentNode) placeholderSpan.remove();
      return;
    }
    if (btnNo) {
      btnNo.classList.remove('btn-no--escaping');
      btnNo.style.position = '';
      btnNo.style.left = '';
      btnNo.style.top = '';
      btnNo.style.margin = '';
      btnNo.onclick = null;
      btnNo.onmouseenter = null;
    }
    if (placeholderSpan && placeholderSpan.parentNode) {
      placeholderSpan.remove();
    }
    if (originalParent && btnNo) {
      if (originalNextSibling && originalNextSibling.parentNode === originalParent) {
        originalParent.insertBefore(btnNo, originalNextSibling);
      } else {
        originalParent.appendChild(btnNo);
      }
    } else if (buttonArea && btnNo) {
      buttonArea.appendChild(btnNo);
    }
    attachNoButtonHoverTrigger();
    isNoEscaping = false;
    placeholderSpan = null;
  }

  function attachNoButtonHoverTrigger() {
    if (!btnNo) return;
    btnNo.removeEventListener('mouseenter', activateEscapeMode);
    btnNo.addEventListener('mouseenter', activateEscapeMode, { once: true });
    btnNo.onclick = (e) => {
      e.stopPropagation();
      if (!isNoEscaping) {
        showGentleMessage('💕 Bạn thử di chuột vào nút "Không" xem nào... nó sẽ chạy đó! 💕');
      } else {
        showGentleMessage('🌸 Đã bảo là không thể từ chối rồi mà! Nhận hoa thôi 🩷');
      }
    };
  }

  function createStars() {
    const starfield = document.getElementById('starfield');
    if (!starfield) return;
    starfield.innerHTML = '';
    for (let i = 0; i < 50; i++) {
      const star = document.createElement('div');
      star.className = 'star';
      const size = 1 + Math.random() * 3;
      star.style.cssText = `width: ${size}px; height: ${size}px; left: ${Math.random() * 100}%; top: ${Math.random() * 100}%; --dur: ${2 + Math.random() * 4}s; --delay: ${Math.random() * 4}s;`;
      starfield.appendChild(star);
    }
  }

  function createSparkles() {
    const layer = document.getElementById('sparkleLayer');
    if (!layer) return;
    layer.innerHTML = '';
    for (let i = 0; i < 20; i++) {
      const s = document.createElement('div');
      s.className = 'sparkle';
      s.style.cssText = `left: ${Math.random() * 100}%; top: ${60 + Math.random() * 40}%; --dur: ${4 + Math.random() * 6}s; --delay: ${Math.random() * 6}s;`;
      layer.appendChild(s);
    }
  }

  let petalInterval = null;
  function showFlower() {
    resetNoButton();
    screenOffer.classList.add('hidden');
    screenFlower.classList.remove('hidden');
    createStars();
    createSparkles();
    setTimeout(spawnPetals, 400);
    setTimeout(spawnPetals, 1400);
    if (petalInterval) clearInterval(petalInterval);
    petalInterval = setInterval(() => {
      const flowerScreen = document.getElementById('screenFlower');
      if (!flowerScreen || flowerScreen.classList.contains('hidden')) return;
      spawnPetals(5);
    }, 700);
  }

  function spawnPetals(count = 15) {
    const colors = ['#ffb3c1', '#ff85a1', '#ffc2d1', '#ff9eb5', '#e94560', '#f48fb1'];
    for (let i = 0; i < count; i++) {
      setTimeout(() => {
        const petal = document.createElement('div');
        petal.className = 'petal';
        petal.innerHTML = `<svg width="${14 + Math.random() * 16}" height="${14 + Math.random() * 16}" viewBox="0 0 20 20"><ellipse cx="10" cy="10" rx="${5 + Math.random() * 5}" ry="${8 + Math.random() * 6}" fill="${colors[Math.floor(Math.random() * colors.length)]}"/></svg>`;
        petal.style.left = Math.random() * 100 + 'vw';
        petal.style.top = '-30px';
        petal.style.animationDuration = (3 + Math.random() * 4) + 's';
        petal.style.animationDelay = Math.random() * 0.5 + 's';
        document.body.appendChild(petal);
        setTimeout(() => petal.remove(), 8000);
      }, i * 60);
    }
  }

  function restart() {
    if (petalInterval) {
      clearInterval(petalInterval);
      petalInterval = null;
    }
    resetNoButton();
    attachNoButtonHoverTrigger();
    screenFlower.classList.add('hidden');
    screenOffer.classList.remove('hidden');
  }

  btnYes.onclick = () => { showFlower(); };
  restartBtn.onclick = () => { restart(); };
  attachNoButtonHoverTrigger();
  btnNo.onclick = (e) => {
    e.stopPropagation();
    if (!isNoEscaping) {
      showGentleMessage('💌 Đừng từ chối nhanh thế! Hãy di chuột vào nút "Không" để thấy điều bất ngờ 💌');
    } else {
      showGentleMessage('🎈 Nút này không thích bị từ chối đâu, hãy nhận hoa nhé! 🎈');
    }
  };

  window.addEventListener('resize', () => {
    if (isNoEscaping && btnNo && btnNo.classList.contains('btn-no--escaping')) {
      const maxX = window.innerWidth - btnNo.offsetWidth - 10;
      const maxY = window.innerHeight - btnNo.offsetHeight - 10;
      let left = parseFloat(btnNo.style.left);
      let top = parseFloat(btnNo.style.top);
      if (isNaN(left)) left = 50;
      if (isNaN(top)) top = 100;
      left = Math.min(Math.max(left, 10), maxX);
      top = Math.min(Math.max(top, 10), maxY);
      btnNo.style.left = left + 'px';
      btnNo.style.top = top + 'px';
    }
  });
</script>
</body>
</html>
""")

st.markdown("""
<style>
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp > footer,
    .stApp > header {
        display: none;
    }
    [data-testid="stMainBlockContainer"] {
        padding: 0 !important;
        max-width: 100% !important;
    }
    [data-testid="stHTML"] > div {
        height: 100vh !important;
        overflow: hidden !important;
    }
</style>
""", unsafe_allow_html=True)
