#!/usr/bin/env python3
"""Generate assets/banner.svg: the animated product journey.

One SVG, no JS, renders inside GitHub's <img>. Every scene shares one frame
(device panel | agent | outcome panel) and lasts SCENE seconds; the loop is
len(SCENES) * SCENE. Inner animations use a SCENE-second period, so they are
always at phase 0 when their scene appears. The static frame (no animation,
reduced motion, rsvg) is scene 1 in its end state.

Run: python3 tools/gen_banner.py   (from the repo root)
"""
from html import escape
from pathlib import Path
from scenes import SCENES

SCENE = 7.0
N = len(SCENES)
LOOP = SCENE * N
W, H = 1280, 470
WIN = 100 / N                      # one scene's share of the loop, in %
FADE = 0.4 / LOOP * 100            # crossfade, in %
SHIELD = "M12 2L4 5v6c0 5 3.4 8.5 8 11 4.6-2.5 8-6 8-11V5l-8-3z"
ORANGE, RED, WHITE = "#FF9A08", "#FF6B6B", "#FFFFFF"


def pct(x):
    return f"{x:.3f}%"


def style():
    show = (f"@keyframes show{{0%{{opacity:0}}{pct(FADE)}{{opacity:1}}"
            f"{pct(WIN - FADE)}{{opacity:1}}{pct(WIN)},100%{{opacity:0}}}}")
    prog = (f"@keyframes prog{{0%{{transform:scaleX(0)}}{pct(WIN)}{{transform:scaleX(1)}}"
            f"{pct(WIN + 0.01)},100%{{transform:scaleX(0)}}}}")
    delays = "".join(f".k{i}{{animation-delay:{i * SCENE:g}s}}" for i in range(N))
    return f"""<style>
    .sans{{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}}
    .mono{{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,"Liberation Mono",monospace}}
    .scene,.chipon{{animation:show {LOOP:g}s linear infinite both}}
    .bar{{transform-box:fill-box;transform-origin:left center;animation:prog {LOOP:g}s linear infinite both}}
    {delays}
    .pii{{animation:detect {SCENE:g}s ease-in-out infinite both}}
    .out{{animation:arrive {SCENE:g}s ease-out infinite both}}
    .flow{{animation:flow 1s linear infinite}}
    .scan{{animation:scan {SCENE:g}s ease-in-out infinite both}}
    .pop{{transform-box:fill-box;transform-origin:center;animation:pop {SCENE:g}s ease-out infinite both}}
    .late{{animation:arrive {SCENE:g}s ease-out 1.6s infinite both}}
    .q1{{animation-delay:.3s}}.q2{{animation-delay:.6s}}.q3{{animation-delay:.9s}}
    {show}
    {prog}
    @keyframes detect{{0%,12%{{fill:{WHITE}}}18%,94%{{fill:{ORANGE}}}100%{{fill:{WHITE}}}}}
    @keyframes arrive{{0%,44%{{opacity:0;transform:translateX(-12px)}}52%,100%{{opacity:1;transform:translateX(0)}}}}
    @keyframes flow{{to{{stroke-dashoffset:-20}}}}
    @keyframes scan{{0%,22%{{opacity:0;transform:translateY(0)}}24%{{opacity:.9}}36%{{opacity:.9;transform:translateY(17px)}}39%,100%{{opacity:0;transform:translateY(17px)}}}}
    @keyframes pop{{0%,38%{{opacity:0;transform:scale(0)}}43%{{opacity:1;transform:scale(1.3)}}47%,100%{{opacity:1;transform:scale(1)}}}}
    @media (prefers-reduced-motion:reduce){{*{{animation:none!important}}.scan{{opacity:0}}.k0.scene,.k0.chipon{{opacity:1}}.bar{{display:none}}}}
  </style>"""


def text_line(x, y, segs, cls=""):
    if segs and segs[0][0] == "late":
        segs, cls = segs[1:], "late"
    out, k = [], 0
    for kind, s in segs:
        s = escape(s)
        if kind == "pii":
            out.append(f'<tspan class="pii{" q%d" % k if k else ""}" fill="{ORANGE}">{s}</tspan>')
            k += 1
        elif kind == "tok":
            out.append(f'<tspan fill="{ORANGE}" font-weight="700">{s}</tspan>')
        elif kind == "red":
            out.append(f'<tspan fill="{RED}" font-weight="700">{s}</tspan>')
        elif kind == "dim":
            out.append(f'<tspan fill-opacity=".6">{s}</tspan>')
        else:
            out.append(s)
    c = f' class="mono {cls}"' if cls else ' class="mono"'
    return f'<text{c} x="{x}" y="{y}" font-size="17" fill="{WHITE}" xml:space="preserve">{"".join(out)}</text>'


def badge(kind):
    # Sits on the shield's lower right, in the shield group's 24-unit space.
    if kind == "dots":
        return "".join(f'<circle class="pop{" q%d" % i if i else ""}" cx="{c}" cy="12.3" r="0.6" fill="{ORANGE}"/>'
                       for i, c in enumerate((13.15, 14.75, 16.35)))
    col, glyph = {"block": (RED, '<path d="M-1.6 -1.6L1.6 1.6" stroke="#fff" stroke-width=".8" stroke-linecap="round"/>'
                                     '<path d="M1.6 -1.6L-1.6 1.6" stroke="#fff" stroke-width=".8" stroke-linecap="round"/>'),
                  "flag": (ORANGE, '<path d="M0 -1.7V0.5" stroke="#fff" stroke-width=".8" stroke-linecap="round"/>'
                                   '<circle cx="0" cy="1.6" r=".45" fill="#fff"/>'),
                  "check": ("#22A06B", '<path d="M-1.5 0.1L-0.4 1.2L1.6 -1.1" fill="none" stroke="#fff" stroke-width=".8" stroke-linecap="round" stroke-linejoin="round"/>')}[kind]
    return f'<g transform="translate(19,18)"><g class="pop"><circle r="3.2" fill="{col}" stroke="#005EB8" stroke-width=".6"/>{glyph}</g></g>'


def scene(i, sc):
    lid = f"k{i}"
    base = "" if i == 0 else ' opacity="0"'
    out_col = {"dots": ORANGE, "block": RED}.get(sc["badge"], WHITE)
    rows = [250, 284, 318, 352]
    left = "\n    ".join(text_line(84, rows[j], segs) for j, segs in enumerate(sc["left"]))
    right = "\n    ".join(text_line(760, rows[j], segs, f"out{' q%d' % j if j else ''}") for j, segs in enumerate(sc["right"]))
    mid_x2 = ('<animate attributeName="x2" values="16.3;16.3;11.3;11.3" keyTimes="0;0.38;0.43;1" dur="%gs" repeatCount="indefinite"/>' % SCENE
              if sc["badge"] == "dots" else "")
    mid_end = "11.3" if sc["badge"] == "dots" else "16.3"
    connector = (f'<line class="flow" x1="692" y1="282" x2="728" y2="282" stroke="{out_col}" stroke-width="3" stroke-dasharray="6 4" stroke-linecap="round"/>')
    if sc["badge"] == "block":
        connector = (f'<line x1="692" y1="282" x2="728" y2="282" stroke="{RED}" stroke-width="3" stroke-dasharray="6 4" stroke-linecap="round" stroke-opacity=".5"/>'
                     f'<g transform="translate(710,282)"><g class="pop"><path d="M-6 -6L6 6M6 -6L-6 6" stroke="{RED}" stroke-width="3.5" stroke-linecap="round"/></g></g>')
    return f"""
  <g class="scene {lid}"{base}>
    <text class="sans" x="84" y="212" font-size="13" font-weight="600" letter-spacing="1.5" fill="{WHITE}" fill-opacity="0.7">{escape(sc["left_label"])}</text>
    {left}
    <text class="sans" x="760" y="212" font-size="13" font-weight="600" letter-spacing="1.5" fill="{WHITE}" fill-opacity="0.7">{escape(sc["right_label"])}</text>
    {right}
    {connector}
    <g transform="translate(568,206) scale(6)">
      <path d="{SHIELD}" fill="#FFFFFF" fill-opacity="0.12" stroke="#FFFFFF" stroke-width="1.1" stroke-linejoin="round"/>
      <g clip-path="url(#sh)"><rect class="scan" x="3" y="3.2" width="18" height="0.45" fill="#FFFFFF" opacity="0"/></g>
      <line x1="7.7" y1="9.3" x2="16.3" y2="9.3" stroke="#FFFFFF" stroke-width="1.2" stroke-linecap="round"/>
      <line x1="7.7" y1="12.3" x2="{mid_end}" y2="12.3" stroke="#FFFFFF" stroke-opacity="0.8" stroke-width="1.2" stroke-linecap="round">{mid_x2}</line>
      <line x1="8.6" y1="15.2" x2="13.2" y2="15.2" stroke="#FFFFFF" stroke-opacity="0.4" stroke-width="1.1" stroke-linecap="round"/>
      {badge(sc["badge"])}
    </g>
    <text class="sans" x="640" y="378" font-size="13" font-weight="600" letter-spacing="1.5" fill="{WHITE}" fill-opacity="0.75" text-anchor="middle">{escape(sc["verb"])}</text>
  </g>"""


def chips():
    gap, x0, w = 10, 60, (1160 - 10 * (N - 1)) / N
    out = []
    for i, sc in enumerate(SCENES):
        x = x0 + i * (w + gap)
        base = "" if i == 0 else ' opacity="0"'
        out.append(f"""
  <rect x="{x:.1f}" y="404" width="{w:.1f}" height="38" rx="9" fill="#FFFFFF" fill-opacity="0.07"/>
  <rect class="chipon k{i}" x="{x:.1f}" y="404" width="{w:.1f}" height="38" rx="9" fill="#FFFFFF" fill-opacity="0.2"{base}/>
  <rect class="bar k{i}" x="{x + 10:.1f}" y="436" width="{w - 20:.1f}" height="3" rx="1.5" fill="{ORANGE}"/>
  <text class="sans" x="{x + w / 2:.1f}" y="428" font-size="13" font-weight="600" fill="#FFFFFF" text-anchor="middle"><tspan fill-opacity=".55">{i + 1:02d}</tspan>  {escape(sc["chip"])}</text>""")
    return "".join(out)


def main():
    alt = ("ScienceSoft Endpoint AI Firewall, shown as a journey: " +
           "; ".join(f'{sc["chip"]}: {sc["alt"]}' for sc in SCENES) + ".")
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{escape(alt)}">
  <title>ScienceSoft Endpoint AI Firewall</title>
  <!-- GENERATED by tools/gen_banner.py from tools/scenes.py. Edit those, not this file.
       Synthetic data only. -->
  {style()}
  <defs><clipPath id="sh"><path d="{SHIELD}"/></clipPath></defs>
  <rect width="{W}" height="{H}" rx="20" fill="#005EB8"/>
  <g transform="translate(60,44) scale(4)">
    <path d="{SHIELD}" fill="#FFFFFF" fill-opacity="0.12" stroke="#FFFFFF" stroke-width="1.5" stroke-linejoin="round"/>
    <line x1="7.7" y1="9.3" x2="16.3" y2="9.3" stroke="#FFFFFF" stroke-width="1.5" stroke-linecap="round"/>
    <line x1="7.7" y1="12.3" x2="11.3" y2="12.3" stroke="#FFFFFF" stroke-opacity="0.8" stroke-width="1.5" stroke-linecap="round"/>
    <circle cx="13.15" cy="12.3" r="0.7" fill="{ORANGE}"/><circle cx="14.75" cy="12.3" r="0.7" fill="{ORANGE}"/><circle cx="16.35" cy="12.3" r="0.7" fill="{ORANGE}"/>
    <line x1="8.6" y1="15.2" x2="13.2" y2="15.2" stroke="#FFFFFF" stroke-opacity="0.4" stroke-width="1.4" stroke-linecap="round"/>
  </g>
  <text class="sans" x="172" y="98" font-size="40" font-weight="700" fill="#FFFFFF">ScienceSoft Endpoint AI Firewall</text>
  <text class="sans" x="172" y="136" font-size="20" fill="#FFFFFF" fill-opacity="0.85">On-device protection for every prompt your people send to AI.</text>
  <text class="sans" x="1220" y="64" font-size="15" fill="#FFFFFF" fill-opacity="0.7" text-anchor="end">by ScienceSoft</text>
  <rect x="60" y="180" width="484" height="196" rx="14" fill="#003F7D" fill-opacity="0.55"/>
  <rect x="736" y="180" width="484" height="196" rx="14" fill="#003F7D" fill-opacity="0.55"/>
  <line class="flow" x1="552" y1="282" x2="588" y2="282" stroke="#FFFFFF" stroke-opacity="0.7" stroke-width="3" stroke-dasharray="6 4" stroke-linecap="round"/>
  {"".join(scene(i, s) for i, s in enumerate(SCENES))}
  {chips()}
</svg>
"""
    for i, sc in enumerate(SCENES):
        for side in ("left", "right"):
            for segs in sc[side]:
                n = sum(len(s) for k, s in segs if k != "late")
                assert n <= 40, f"scene {i + 1} {side} line too long ({n}): {segs}"
            assert len(sc[side]) <= 4, f"scene {i + 1} {side} has more than 4 lines"
    Path(__file__).resolve().parent.parent.joinpath("assets/banner.svg").write_text(svg)
    print(f"wrote assets/banner.svg: {N} scenes, {LOOP:g}s loop")


if __name__ == "__main__":
    main()
