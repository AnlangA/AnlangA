#!/usr/bin/env python3
"""Generate bespoke architectural SVG assets for AnlangA's GitHub Profile README."""

from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)

FONT_SANS = "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif"
FONT_MONO = "'JetBrains Mono', 'Fira Code', 'SF Mono', 'Cascadia Code', Consolas, monospace"


def write_svg(filename: str, content: str) -> None:
    content = content.strip() + "\n"
    ET.fromstring(content)
    path = ASSETS / filename
    path.write_text(content, encoding="utf-8")
    print(f"Generated & validated: {path.relative_to(ROOT)} ({len(content)} bytes)")


def generate_hero_banner() -> None:
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 304" width="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080A0F"/>
      <stop offset="48%" stop-color="#0D1119"/>
      <stop offset="100%" stop-color="#090C12"/>
    </linearGradient>
    <radialGradient id="amberGlow" cx="84%" cy="24%" r="50%">
      <stop offset="0%" stop-color="#E06C3A" stop-opacity="0.18"/>
      <stop offset="55%" stop-color="#E06C3A" stop-opacity="0.04"/>
      <stop offset="100%" stop-color="#E06C3A" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="cyanGlow" cx="14%" cy="88%" r="45%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.10"/>
      <stop offset="60%" stop-color="#38BDF8" stop-opacity="0.02"/>
      <stop offset="100%" stop-color="#38BDF8" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="topEdge" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1E2536" stop-opacity="0.2"/>
      <stop offset="25%" stop-color="#E06C3A" stop-opacity="0.75"/>
      <stop offset="65%" stop-color="#38BDF8" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#1E2536" stop-opacity="0.2"/>
    </linearGradient>
    <linearGradient id="amberAccent" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#F0883E"/>
      <stop offset="100%" stop-color="#D9602B"/>
    </linearGradient>
    <style>
      .sans {{ font-family: {FONT_SANS}; }}
      .mono {{ font-family: {FONT_MONO}; }}
      @keyframes pulse {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0.35; }}
      }}
      @keyframes orbit {{
        0%, 100% {{ stroke-dashoffset: 0; }}
        50% {{ stroke-dashoffset: 24; }}
      }}
      .pulse-dot {{ animation: pulse 2.6s ease-in-out infinite; }}
      .orbit-ring {{ animation: orbit 8s linear infinite; }}
    </style>
  </defs>

  <!-- Main Card Frame -->
  <rect x="1" y="1" width="878" height="302" rx="14" fill="url(#bgGrad)" stroke="#1E2534" stroke-width="1.2"/>
  <rect x="1" y="1" width="878" height="302" rx="14" fill="url(#amberGlow)"/>
  <rect x="1" y="1" width="878" height="302" rx="14" fill="url(#cyanGlow)"/>

  <!-- Top Specular Highlight Line -->
  <rect x="24" y="1" width="832" height="1.5" fill="url(#topEdge)"/>

  <!-- Subtle Architectural CAD Corner Crosshairs -->
  <g stroke="#2B3548" stroke-width="1" fill="none">
    <path d="M 18 26 L 18 18 L 26 18"/>
    <path d="M 862 26 L 862 18 L 854 18"/>
    <path d="M 18 278 L 18 286 L 26 286"/>
    <path d="M 862 278 L 862 286 L 854 286"/>
  </g>

  <!-- Right-Side Schematic Topology Graphic -->
  <g transform="translate(744, 126)" opacity="0.34">
    <circle cx="0" cy="0" r="78" fill="none" stroke="#E06C3A" stroke-width="1" stroke-dasharray="4 6" class="orbit-ring"/>
    <circle cx="0" cy="0" r="54" fill="none" stroke="#38BDF8" stroke-width="0.9" stroke-opacity="0.7"/>
    <circle cx="0" cy="0" r="28" fill="none" stroke="#8B949E" stroke-width="0.8" stroke-dasharray="2 4"/>
    <line x1="-88" y1="0" x2="88" y2="0" stroke="#212836" stroke-width="1"/>
    <line x1="0" y1="-88" x2="0" y2="88" stroke="#212836" stroke-width="1"/>
    <circle cx="0" cy="0" r="4" fill="#E06C3A"/>
    <circle cx="54" cy="0" r="3" fill="#38BDF8"/>
    <circle cx="-38" cy="-38" r="2.5" fill="#10B981"/>
    <circle cx="38" cy="38" r="2.5" fill="#F59E0B"/>
  </g>

  <!-- Top Telemetry Header Bar -->
  <text x="40" y="38" class="mono" font-size="11" fill="#6E7681" letter-spacing="2">SYS.ARCH // ANLANGA.PORTFOLIO</text>

  <g transform="translate(646, 22)">
    <rect x="0" y="0" width="194" height="22" rx="11" fill="#111622" stroke="#232C3D" stroke-width="1"/>
    <circle cx="15" cy="11" r="3.5" fill="#10B981" class="pulse-dot"/>
    <text x="27" y="14.5" class="mono" font-size="10" fill="#C9D1D9" letter-spacing="1">SYSTEMS ONLINE</text>
    <text x="142" y="14.5" class="mono" font-size="10" fill="#E06C3A" font-weight="600">CN · 2026</text>
  </g>

  <line x1="40" y1="54" x2="840" y2="54" stroke="#19202E" stroke-width="1"/>

  <!-- Hero Identity -->
  <text x="40" y="102" class="sans" font-size="38" font-weight="800" fill="#F0F6FC" letter-spacing="-0.6">Stone Mason</text>
  <g transform="translate(292, 76)">
    <rect x="0" y="0" width="96" height="24" rx="6" fill="#1A1516" stroke="#E06C3A" stroke-width="1" stroke-opacity="0.6"/>
    <text x="48" y="16" class="mono" font-size="12" font-weight="600" fill="#F0883E" text-anchor="middle">@AnlangA</text>
  </g>

  <!-- Bilingual Executive Positioning -->
  <text x="40" y="132" class="sans" font-size="15" font-weight="600" fill="#E6EDF3">
    Systems &amp; Embedded Rust Architect
    <tspan fill="#484F58" dx="8">·</tspan>
    <tspan fill="#9CA3AF" font-weight="400" dx="8">系统级 Rust / 嵌入式 Linux BSP / 大模型基建 / 工业协议工程</tspan>
  </text>

  <!-- Philosophy / Engineering Statement -->
  <rect x="40" y="149" width="3" height="38" rx="1.5" fill="url(#amberAccent)"/>
  <text x="54" y="164" class="mono" font-size="11.5" fill="#9CA3AF">
    "Memory safety without garbage collection; deterministic control from bare-metal MCUs to cloud LLM gateways."
  </text>
  <text x="54" y="183" class="sans" font-size="12" fill="#6E7681">
    深耕高可靠嵌入式系统（RK3588 / GD32H7 / ESP32-S3）、工业现场总线（EtherCAT / Modbus / OCPP）与纯 Rust AI 基础设施。
  </text>

  <!-- Bottom 4-Column Architectural Spec Strip (3 stacked lines per column -> zero horizontal collision) -->
  <line x1="40" y1="206" x2="840" y2="206" stroke="#1B2232" stroke-width="1"/>

  <!-- Column 1 -->
  <g transform="translate(40, 220)">
    <text x="0" y="11" class="mono" font-size="10" fill="#6E7681" letter-spacing="1.2">01 // CORE LANGUAGES</text>
    <text x="0" y="33" class="sans" font-size="15.5" font-weight="700" fill="#F0F6FC">Rust · C · C++</text>
    <text x="0" y="51" class="mono" font-size="11" fill="#E06C3A">Edition 2024 · no_std &amp; Async</text>
  </g>

  <line x1="242" y1="216" x2="242" y2="278" stroke="#1B2232" stroke-width="1"/>

  <!-- Column 2 -->
  <g transform="translate(262, 220)">
    <text x="0" y="11" class="mono" font-size="10" fill="#6E7681" letter-spacing="1.2">02 // SILICON &amp; KERNEL BSP</text>
    <text x="0" y="33" class="sans" font-size="15.5" font-weight="700" fill="#F0F6FC">RK3588 · GD32H7 · ESP32</text>
    <text x="0" y="51" class="mono" font-size="11" fill="#38BDF8">Mainline Linux v7.2 · Zephyr</text>
  </g>

  <line x1="478" y1="216" x2="478" y2="278" stroke="#1B2232" stroke-width="1"/>

  <!-- Column 3 -->
  <g transform="translate(498, 220)">
    <text x="0" y="11" class="mono" font-size="10" fill="#6E7681" letter-spacing="1.2">03 // INDUSTRIAL &amp; AI INFRA</text>
    <text x="0" y="33" class="sans" font-size="15.5" font-weight="700" fill="#F0F6FC">EtherCAT · LLM Gateways</text>
    <text x="0" y="51" class="mono" font-size="11" fill="#10B981">CoE/PDO · Axum 0.8 · Burn GPU</text>
  </g>

  <line x1="710" y1="216" x2="710" y2="278" stroke="#1B2232" stroke-width="1"/>

  <!-- Column 4 -->
  <g transform="translate(730, 220)">
    <text x="0" y="11" class="mono" font-size="10" fill="#6E7681" letter-spacing="1.2">04 // OPEN SOURCE</text>
    <text x="0" y="33" class="sans" font-size="15.5" font-weight="700" fill="#F0F6FC">128 Public Repos</text>
    <text x="0" y="51" class="mono" font-size="11" fill="#F59E0B">58 Original Crates</text>
  </g>
</svg>"""
    write_svg("hero-banner.svg", svg)


def generate_system_architecture() -> None:
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 360" width="100%">
  <defs>
    <linearGradient id="cardBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090C12"/>
      <stop offset="100%" stop-color="#0E121B"/>
    </linearGradient>
    <linearGradient id="quadBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#121723"/>
      <stop offset="100%" stop-color="#0C1018"/>
    </linearGradient>
    <style>
      .sans {{ font-family: {FONT_SANS}; }}
      .mono {{ font-family: {FONT_MONO}; }}
      .pill {{ fill: #151B27; stroke: #252F42; stroke-width: 1; }}
      .pill-amber {{ fill: #1D1514; stroke: #5E3322; stroke-width: 1; }}
      .pill-cyan {{ fill: #101B26; stroke: #1D4463; stroke-width: 1; }}
      .pill-emerald {{ fill: #0F1E1B; stroke: #1A4D40; stroke-width: 1; }}
      .pill-gold {{ fill: #1D1912; stroke: #59431B; stroke-width: 1; }}
    </style>
  </defs>

  <!-- Outer Container -->
  <rect x="1" y="1" width="878" height="358" rx="14" fill="url(#cardBg)" stroke="#1E2534" stroke-width="1.2"/>

  <!-- Section Header (Using single text + tspan so zero overlap is guaranteed) -->
  <text x="28" y="33" class="mono" font-size="11" fill="#E06C3A" font-weight="600">
    01 // ARCHITECTURE MATRIX
    <tspan class="sans" font-size="12.5" fill="#8B949E" font-weight="400" dx="14">四维工程技术体系 · Full-Stack Systems Engineering</tspan>
  </text>
  <text x="852" y="33" class="mono" font-size="10.5" fill="#6E7681" text-anchor="end">SPEC.REV.2026</text>
  <line x1="28" y1="48" x2="852" y2="48" stroke="#1B2230" stroke-width="1"/>

  <!-- ==================== QUADRANT 1: EMBEDDED & LINUX BSP ==================== -->
  <g transform="translate(24, 62)">
    <rect x="0" y="0" width="408" height="132" rx="10" fill="url(#quadBg)" stroke="#1F2737" stroke-width="1"/>
    <rect x="0" y="18" width="3" height="30" rx="1.5" fill="#E06C3A"/>

    <text x="18" y="25" class="mono" font-size="10.5" fill="#E06C3A" font-weight="600">01 · EMBEDDED &amp; KERNEL BSP</text>
    <text x="392" y="25" class="mono" font-size="10" fill="#6E7681" text-anchor="end">裸机 / RTOS / 主线内核</text>
    <text x="18" y="48" class="sans" font-size="15" font-weight="700" fill="#F0F6FC">嵌入式系统与 Linux 板级支持包</text>
    <text x="18" y="68" class="sans" font-size="12" fill="#8B949E">从 Cortex-M7 / RISC-V 微控制器到 RK3588 主线内核 Rust 驱动开发</text>

    <!-- Tech Pills -->
    <g transform="translate(18, 86)">
      <rect x="0" y="0" width="94" height="24" rx="5" class="pill-amber"/>
      <text x="47" y="15.5" class="mono" font-size="11" fill="#F0883E" text-anchor="middle">RK3588 BSP</text>

      <rect x="102" y="0" width="76" height="24" rx="5" class="pill"/>
      <text x="140" y="15.5" class="mono" font-size="11" fill="#C9D1D9" text-anchor="middle">GD32H7</text>

      <rect x="186" y="0" width="80" height="24" rx="5" class="pill"/>
      <text x="226" y="15.5" class="mono" font-size="11" fill="#C9D1D9" text-anchor="middle">ESP32-S3</text>

      <rect x="274" y="0" width="114" height="24" rx="5" class="pill"/>
      <text x="331" y="15.5" class="mono" font-size="11" fill="#9CA3AF" text-anchor="middle">no_std / Zephyr</text>
    </g>
  </g>

  <!-- ==================== QUADRANT 2: AI INFRA & EDGE INFERENCE ==================== -->
  <g transform="translate(448, 62)">
    <rect x="0" y="0" width="408" height="132" rx="10" fill="url(#quadBg)" stroke="#1F2737" stroke-width="1"/>
    <rect x="0" y="18" width="3" height="30" rx="1.5" fill="#38BDF8"/>

    <text x="18" y="25" class="mono" font-size="10.5" fill="#38BDF8" font-weight="600">02 · AI INFRA &amp; EDGE INFERENCE</text>
    <text x="392" y="25" class="mono" font-size="10" fill="#6E7681" text-anchor="end">SDK / 网关 / 端侧部署</text>
    <text x="18" y="48" class="sans" font-size="15" font-weight="700" fill="#F0F6FC">大模型基础设施与端侧异构推理</text>
    <text x="18" y="68" class="sans" font-size="12" fill="#8B949E">纯 Rust 类型安全 LLM SDK 矩阵、高并发代理网关与 Vulkan 量化推理</text>

    <!-- Tech Pills -->
    <g transform="translate(18, 86)">
      <rect x="0" y="0" width="88" height="24" rx="5" class="pill-cyan"/>
      <text x="44" y="15.5" class="mono" font-size="11" fill="#38BDF8" text-anchor="middle">Axum 0.8</text>

      <rect x="96" y="0" width="104" height="24" rx="5" class="pill"/>
      <text x="148" y="15.5" class="mono" font-size="11" fill="#C9D1D9" text-anchor="middle">Zhipu/OpenAI</text>

      <rect x="208" y="0" width="84" height="24" rx="5" class="pill"/>
      <text x="250" y="15.5" class="mono" font-size="11" fill="#C9D1D9" text-anchor="middle">Burn GPU</text>

      <rect x="300" y="0" width="88" height="24" rx="5" class="pill"/>
      <text x="344" y="15.5" class="mono" font-size="11" fill="#9CA3AF" text-anchor="middle">Qwen3 GGUF</text>
    </g>
  </g>

  <!-- ==================== QUADRANT 3: INDUSTRIAL PROTOCOLS ==================== -->
  <g transform="translate(24, 206)">
    <rect x="0" y="0" width="408" height="132" rx="10" fill="url(#quadBg)" stroke="#1F2737" stroke-width="1"/>
    <rect x="0" y="18" width="3" height="30" rx="1.5" fill="#10B981"/>

    <text x="18" y="25" class="mono" font-size="10.5" fill="#10B981" font-weight="600">03 · INDUSTRIAL FIELDBUS &amp; POWER</text>
    <text x="392" y="25" class="mono" font-size="10" fill="#6E7681" text-anchor="end">实时以太网 / 能源协议</text>
    <text x="18" y="48" class="sans" font-size="15" font-weight="700" fill="#F0F6FC">工业总线协议栈与电力电子通信</text>
    <text x="18" y="68" class="sans" font-size="12" fill="#8B949E">EtherCAT 报文剖析与主站控制、ESI/SII 编译、Modbus 及充电机协议</text>

    <!-- Tech Pills -->
    <g transform="translate(18, 86)">
      <rect x="0" y="0" width="92" height="24" rx="5" class="pill-emerald"/>
      <text x="46" y="15.5" class="mono" font-size="11" fill="#34D399" text-anchor="middle">EtherCAT</text>

      <rect x="100" y="0" width="86" height="24" rx="5" class="pill"/>
      <text x="143" y="15.5" class="mono" font-size="11" fill="#C9D1D9" text-anchor="middle">CoE / PDO</text>

      <rect x="194" y="0" width="92" height="24" rx="5" class="pill"/>
      <text x="240" y="15.5" class="mono" font-size="11" fill="#C9D1D9" text-anchor="middle">Modbus TCP</text>

      <rect x="294" y="0" width="94" height="24" rx="5" class="pill"/>
      <text x="341" y="15.5" class="mono" font-size="11" fill="#9CA3AF" text-anchor="middle">OCPP / EXI</text>
    </g>
  </g>

  <!-- ==================== QUADRANT 4: NATIVE GUI & WORKBENCHES ==================== -->
  <g transform="translate(448, 206)">
    <rect x="0" y="0" width="408" height="132" rx="10" fill="url(#quadBg)" stroke="#1F2737" stroke-width="1"/>
    <rect x="0" y="18" width="3" height="30" rx="1.5" fill="#F59E0B"/>

    <text x="18" y="25" class="mono" font-size="10.5" fill="#F59E0B" font-weight="600">04 · NATIVE GUI WORKBENCHES</text>
    <text x="392" y="25" class="mono" font-size="10" fill="#6E7681" text-anchor="end">高帧率渲染 / 研发工具</text>
    <text x="18" y="48" class="sans" font-size="15" font-weight="700" fill="#F0F6FC">高性能原生桌面与工程调试软件</text>
    <text x="18" y="68" class="sans" font-size="12" fill="#8B949E">基于 egui 与 Bevy 引擎打造低延迟串口波形仪、XML/EXI 及证书工作台</text>

    <!-- Tech Pills -->
    <g transform="translate(18, 86)">
      <rect x="0" y="0" width="96" height="24" rx="5" class="pill-gold"/>
      <text x="48" y="15.5" class="mono" font-size="11" fill="#FBBF24" text-anchor="middle">egui/eframe</text>

      <rect x="104" y="0" width="92" height="24" rx="5" class="pill"/>
      <text x="150" y="15.5" class="mono" font-size="11" fill="#C9D1D9" text-anchor="middle">Bevy Engine</text>

      <rect x="204" y="0" width="92" height="24" rx="5" class="pill"/>
      <text x="250" y="15.5" class="mono" font-size="11" fill="#C9D1D9" text-anchor="middle">Serial/Plot</text>

      <rect x="304" y="0" width="84" height="24" rx="5" class="pill"/>
      <text x="346" y="15.5" class="mono" font-size="11" fill="#9CA3AF" text-anchor="middle">X.509/EXI</text>
    </g>
  </g>
</svg>"""
    write_svg("system-architecture.svg", svg)


def generate_telemetry_stats() -> None:
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 268" width="100%">
  <defs>
    <linearGradient id="tBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090C12"/>
      <stop offset="100%" stop-color="#0E121B"/>
    </linearGradient>
    <linearGradient id="panelBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#121723"/>
      <stop offset="100%" stop-color="#0C1018"/>
    </linearGradient>
    <linearGradient id="rustBar" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#E06C3A"/>
      <stop offset="100%" stop-color="#F59E0B"/>
    </linearGradient>
    <linearGradient id="cBar" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0284C7"/>
      <stop offset="100%" stop-color="#38BDF8"/>
    </linearGradient>
    <linearGradient id="tsBar" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#34D399"/>
    </linearGradient>
    <style>
      .sans {{ font-family: {FONT_SANS}; }}
      .mono {{ font-family: {FONT_MONO}; }}
    </style>
  </defs>

  <!-- Outer Frame -->
  <rect x="1" y="1" width="878" height="266" rx="14" fill="url(#tBg)" stroke="#1E2534" stroke-width="1.2"/>

  <!-- Header (Single text + tspan so zero overlap is guaranteed) -->
  <text x="28" y="33" class="mono" font-size="11" fill="#38BDF8" font-weight="600">
    02 // CODEBASE TELEMETRY &amp; LANGUAGE SPECTRUM
    <tspan class="sans" font-size="12.5" fill="#8B949E" font-weight="400" dx="14">研发遥测与代码生态占比</tspan>
  </text>
  <text x="852" y="33" class="mono" font-size="10.5" fill="#6E7681" text-anchor="end">58 ORIGINAL / 128 PUBLIC REPOS</text>
  <line x1="28" y1="48" x2="852" y2="48" stroke="#1B2230" stroke-width="1"/>

  <!-- Left Panel: Key Engineering Metrics -->
  <g transform="translate(24, 62)">
    <rect x="0" y="0" width="380" height="184" rx="10" fill="url(#panelBg)" stroke="#1F2737" stroke-width="1"/>

    <text x="20" y="25" class="mono" font-size="10.5" fill="#8B949E">GITHUB TELEMETRY · 关键仓库指标</text>
    <text x="360" y="25" class="mono" font-size="10" fill="#10B981" text-anchor="end">● VERIFIED</text>
    <line x1="20" y1="36" x2="360" y2="36" stroke="#1B2230" stroke-width="1"/>

    <!-- Row 1 -->
    <g transform="translate(20, 50)">
      <text x="0" y="12" class="mono" font-size="10" fill="#6E7681">PUBLIC REPOS</text>
      <text x="0" y="38" class="mono" font-size="25" font-weight="700" fill="#F0F6FC">128</text>
    </g>
    <g transform="translate(142, 50)">
      <text x="0" y="12" class="mono" font-size="10" fill="#6E7681">ORIGINAL CRATES</text>
      <text x="0" y="38" class="mono" font-size="25" font-weight="700" fill="#E06C3A">58</text>
    </g>
    <g transform="translate(264, 50)">
      <text x="0" y="12" class="mono" font-size="10" fill="#6E7681">RUST RATIO</text>
      <text x="0" y="38" class="mono" font-size="25" font-weight="700" fill="#38BDF8">69.0%</text>
    </g>

    <line x1="20" y1="104" x2="360" y2="104" stroke="#19202D" stroke-width="1" stroke-dasharray="3 3"/>

    <!-- Row 2 -->
    <g transform="translate(20, 118)">
      <text x="0" y="12" class="mono" font-size="10" fill="#6E7681">RUST EDITION</text>
      <text x="0" y="34" class="sans" font-size="14.5" font-weight="700" fill="#C9D1D9">2021 / 2024</text>
    </g>
    <g transform="translate(142, 118)">
      <text x="0" y="12" class="mono" font-size="10" fill="#6E7681">KERNEL TARGET</text>
      <text x="0" y="34" class="sans" font-size="14.5" font-weight="700" fill="#C9D1D9">Linux v7.2 BSP</text>
    </g>
    <g transform="translate(264, 118)">
      <text x="0" y="12" class="mono" font-size="10" fill="#6E7681">COMMUNITY</text>
      <text x="0" y="34" class="mono" font-size="14.5" font-weight="700" fill="#10B981">★ 23 · 19 Flw</text>
    </g>
  </g>

  <!-- Right Panel: Precision Language Breakdown -->
  <g transform="translate(420, 62)">
    <rect x="0" y="0" width="436" height="184" rx="10" fill="url(#panelBg)" stroke="#1F2737" stroke-width="1"/>

    <text x="20" y="25" class="mono" font-size="10.5" fill="#8B949E">LANGUAGE SPECTRUM · 原创项目语言分布</text>
    <text x="416" y="25" class="mono" font-size="10" fill="#E06C3A" text-anchor="end">SYSTEMS-FIRST</text>

    <!-- Stacked Multi-Segment Master Bar (width = 396) -->
    <g transform="translate(20, 36)">
      <rect x="0" y="0" width="396" height="10" rx="5" fill="#181F2C"/>
      <rect x="0" y="0" width="273" height="10" rx="4" fill="url(#rustBar)"/>
      <rect x="275" y="0" width="55" height="10" fill="url(#cBar)"/>
      <rect x="332" y="0" width="21" height="10" fill="#F59E0B"/>
      <rect x="355" y="0" width="41" height="10" rx="4" fill="url(#tsBar)"/>
    </g>

    <!-- Row 1: Rust -->
    <g transform="translate(20, 66)">
      <circle cx="6" cy="-4" r="4.5" fill="#E06C3A"/>
      <text x="18" y="0" class="sans" font-size="13" font-weight="700" fill="#F0F6FC">Rust</text>
      <text x="60" y="0" class="mono" font-size="11" fill="#8B949E">40 repos · SDKs / BSP / EtherCAT / GUI</text>
      <text x="396" y="0" class="mono" font-size="12" font-weight="700" fill="#F0883E" text-anchor="end">69.0%</text>
      <rect x="0" y="7" width="396" height="4" rx="2" fill="#171D29"/>
      <rect x="0" y="7" width="273" height="4" rx="2" fill="url(#rustBar)"/>
    </g>

    <!-- Row 2: C / C++ -->
    <g transform="translate(20, 99)">
      <circle cx="6" cy="-4" r="4.5" fill="#38BDF8"/>
      <text x="18" y="0" class="sans" font-size="13" font-weight="700" fill="#F0F6FC">C / C++</text>
      <text x="78" y="0" class="mono" font-size="11" fill="#8B949E">8 repos · GD32 Bootloader / Power Drivers</text>
      <text x="396" y="0" class="mono" font-size="12" font-weight="700" fill="#38BDF8" text-anchor="end">13.8%</text>
      <rect x="0" y="7" width="396" height="4" rx="2" fill="#171D29"/>
      <rect x="0" y="7" width="55" height="4" rx="2" fill="url(#cBar)"/>
    </g>

    <!-- Row 3: Python -->
    <g transform="translate(20, 132)">
      <circle cx="6" cy="-4" r="4.5" fill="#F59E0B"/>
      <text x="18" y="0" class="sans" font-size="13" font-weight="700" fill="#F0F6FC">Python</text>
      <text x="74" y="0" class="mono" font-size="11" fill="#8B949E">3 repos · Qwen3 GGUF Quant / ART-Pi Zephyr</text>
      <text x="396" y="0" class="mono" font-size="12" font-weight="700" fill="#FBBF24" text-anchor="end">5.2%</text>
      <rect x="0" y="7" width="396" height="4" rx="2" fill="#171D29"/>
      <rect x="0" y="7" width="24" height="4" rx="2" fill="#F59E0B"/>
    </g>

    <!-- Row 4: TypeScript / Typst / Just -->
    <g transform="translate(20, 165)">
      <circle cx="6" cy="-4" r="4.5" fill="#10B981"/>
      <text x="18" y="0" class="sans" font-size="13" font-weight="700" fill="#F0F6FC">TypeScript · Typst · Just</text>
      <text x="186" y="0" class="mono" font-size="11" fill="#8B949E">7 repos · BBCom / Specs</text>
      <text x="396" y="0" class="mono" font-size="12" font-weight="700" fill="#34D399" text-anchor="end">12.0%</text>
    </g>
  </g>
</svg>"""
    write_svg("telemetry-stats.svg", svg)


def generate_project_card(
    filename: str,
    index: str,
    category: str,
    accent: str,
    repo_name: str,
    stars: str,
    lang: str,
    lang_color: str,
    desc_line1: str,
    desc_line2: str,
    tags: list[str],
) -> None:
    tag_elements = []
    x_cursor = 22
    for t in tags:
        width = max(len(t) * 6.8 + 16, 54)
        tag_elements.append(
            f'<rect x="{x_cursor:.1f}" y="122" width="{width:.1f}" height="22" rx="5" fill="#141A26" stroke="#242E42" stroke-width="1"/>'
            f'<text x="{x_cursor + width / 2:.1f}" y="136.5" class="mono" font-size="10.5" fill="#9CA3AF" text-anchor="middle">{t}</text>'
        )
        x_cursor += width + 8

    tags_svg = "\n  ".join(tag_elements)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 432 162" width="100%">
  <defs>
    <linearGradient id="pBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0B0E16"/>
      <stop offset="100%" stop-color="#101521"/>
    </linearGradient>
    <style>
      .sans {{ font-family: {FONT_SANS}; }}
      .mono {{ font-family: {FONT_MONO}; }}
    </style>
  </defs>

  <!-- Card Frame -->
  <rect x="1" y="1" width="430" height="160" rx="12" fill="url(#pBg)" stroke="#1F2737" stroke-width="1.2"/>
  <rect x="1" y="20" width="3" height="32" rx="1.5" fill="{accent}"/>

  <!-- Top Category & Star Row -->
  <text x="22" y="28" class="mono" font-size="10" fill="{accent}" letter-spacing="1.2" font-weight="600">{index} // {category}</text>

  <g transform="translate(352, 14)">
    <rect x="0" y="0" width="58" height="20" rx="10" fill="#151B28" stroke="#263147" stroke-width="1"/>
    <text x="29" y="13.5" class="mono" font-size="10.5" fill="#FBBF24" text-anchor="middle" font-weight="600">★ {stars}</text>
  </g>

  <!-- Repo Title -->
  <text x="22" y="54" class="sans" font-size="17" font-weight="800" fill="#F0F6FC" letter-spacing="-0.2">{repo_name}</text>

  <!-- Description Lines -->
  <text x="22" y="79" class="sans" font-size="12.5" fill="#C9D1D9">{desc_line1}</text>
  <text x="22" y="99" class="sans" font-size="11.5" fill="#8B949E">{desc_line2}</text>

  <line x1="22" y1="112" x2="410" y2="112" stroke="#1A2130" stroke-width="1"/>

  <!-- Tech Tags -->
  {tags_svg}

  <!-- Right-Aligned Language Indicator (never clips!) -->
  <text x="410" y="137" class="mono" font-size="11" fill="#8B949E" text-anchor="end">
    <tspan fill="{lang_color}">●</tspan> {lang}
  </text>
</svg>"""
    write_svg(filename, svg)


def generate_projects_header() -> None:
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 52" width="100%">
  <defs>
    <linearGradient id="hBg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#090C12"/>
      <stop offset="100%" stop-color="#0E121B"/>
    </linearGradient>
    <style>
      .sans {{ font-family: {FONT_SANS}; }}
      .mono {{ font-family: {FONT_MONO}; }}
    </style>
  </defs>
  <rect x="1" y="1" width="878" height="50" rx="12" fill="url(#hBg)" stroke="#1E2534" stroke-width="1.2"/>
  <rect x="1" y="14" width="3" height="24" rx="1.5" fill="#10B981"/>
  <text x="28" y="31" class="mono" font-size="11" fill="#10B981" font-weight="600">
    03 // FLAGSHIP ENGINEERING WORKS
    <tspan class="sans" font-size="12.5" fill="#8B949E" font-weight="400" dx="14">核心开源代表作 · Click any card to inspect repository</tspan>
  </text>
  <text x="852" y="31" class="mono" font-size="10.5" fill="#6E7681" text-anchor="end">SELECTED CRATES [01–06]</text>
</svg>"""
    write_svg("section-projects.svg", svg)


def generate_footer() -> None:
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 84" width="100%">
  <defs>
    <linearGradient id="fBg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#090B10"/>
      <stop offset="50%" stop-color="#101520"/>
      <stop offset="100%" stop-color="#090B10"/>
    </linearGradient>
    <linearGradient id="fLine" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1E2534" stop-opacity="0.1"/>
      <stop offset="50%" stop-color="#E06C3A" stop-opacity="0.55"/>
      <stop offset="100%" stop-color="#1E2534" stop-opacity="0.1"/>
    </linearGradient>
    <style>
      .sans {{ font-family: {FONT_SANS}; }}
      .mono {{ font-family: {FONT_MONO}; }}
    </style>
  </defs>

  <rect x="1" y="1" width="878" height="82" rx="12" fill="url(#fBg)" stroke="#1A202E" stroke-width="1"/>
  <rect x="80" y="1" width="720" height="1.2" fill="url(#fLine)"/>

  <text x="440" y="36" class="sans" font-size="13" font-style="italic" fill="#C9D1D9" text-anchor="middle">
    "Memory safety without garbage collection, concurrency without data races."
  </text>
  <text x="440" y="58" class="mono" font-size="10.5" fill="#6E7681" text-anchor="middle" letter-spacing="2">
    STONE MASON (ANLANGA) · CRAFTED WITH PRECISION IN RUST · 2026
  </text>
</svg>"""
    write_svg("footer-banner.svg", svg)


def main() -> None:
    generate_hero_banner()
    generate_system_architecture()
    generate_telemetry_stats()
    generate_projects_header()

    projects = [
        dict(
            filename="project-bbcom.svg",
            index="01",
            category="EMBEDDED WORKBENCH",
            accent="#E06C3A",
            repo_name="bbcom",
            stars="4",
            lang="TypeScript",
            lang_color="#3178C6",
            desc_line1="跨平台嵌入式串口与工业协议调试工作台",
            desc_line2="支持多会话收发、Modbus 主站、实时波形绘制、宏触发与 AI 诊断",
            tags=["Serial Studio", "Modbus", "Waveform"],
        ),
        dict(
            filename="project-ethercat-cli.svg",
            index="02",
            category="INDUSTRIAL FIELDBUS",
            accent="#10B981",
            repo_name="ethercat-cli",
            stars="1",
            lang="Rust",
            lang_color="#E06C3A",
            desc_line1="纯 Rust 工业 EtherCAT 命令行与多 Crate 核心工作区",
            desc_line2="L2/UDP 报文剖析、ESI-to-SII EEPROM 编译器与 CoE/PDO 主站",
            tags=["EtherCAT", "CoE / PDO", "EEPROM"],
        ),
        dict(
            filename="project-glm-proxy.svg",
            index="03",
            category="AI INFRASTRUCTURE",
            accent="#38BDF8",
            repo_name="glm-proxy",
            stars="3",
            lang="Rust",
            lang_color="#E06C3A",
            desc_line1="基于 Rust + Axum 0.8 构建的高并发大模型 API 透明转发网关",
            desc_line2="支持低延迟流式 SSE 透传、双向协议兼容、链路追踪与高可靠路由",
            tags=["Axum 0.8", "LLM Proxy", "Tokio"],
        ),
        dict(
            filename="project-rk3588-bsp.svg",
            index="04",
            category="MAINLINE LINUX BSP",
            accent="#F59E0B",
            repo_name="atk-dlrk3588-bsp",
            stars="1",
            lang="Rust",
            lang_color="#E06C3A",
            desc_line1="正点原子 RK3588 主线 Linux v7.2.5 / U-Boot 板级支持包",
            desc_line2="板级 DTS 设备树、纯 Rust UART/RS485 字符设备驱动与硬件测试",
            tags=["RK3588", "Linux v7.2", "Rust Driver"],
        ),
        dict(
            filename="project-serial-bevy.svg",
            index="05",
            category="NATIVE GUI ENGINE",
            accent="#E06C3A",
            repo_name="serial_bevy",
            stars="4",
            lang="Rust",
            lang_color="#E06C3A",
            desc_line1="基于 Bevy 游戏引擎架构构建的现代化高性能串口通信工具",
            desc_line2="采用 ECS 数据驱动架构实现低延迟串口收发、监控与高帧率交互",
            tags=["Bevy ECS", "Serial I/O", "Native GUI"],
        ),
        dict(
            filename="project-zai-rs.svg",
            index="06",
            category="PURE-RUST LLM SDK",
            accent="#38BDF8",
            repo_name="zhipuai-rs / zai-rs",
            stars="3",
            lang="Rust",
            lang_color="#E06C3A",
            desc_line1="类型安全、零样板代码的智谱 AI 与大模型生态纯 Rust 客户端库",
            desc_line2="提供完备的异步流式对话、工具调用、强类型建模与一致错误处理",
            tags=["Async SDK", "Type-Safe", "SSE Stream"],
        ),
    ]
    for p in projects:
        generate_project_card(**p)

    generate_footer()


if __name__ == "__main__":
    main()
