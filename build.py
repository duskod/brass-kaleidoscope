#!/usr/bin/env python3
"""Wrap src-artifact.html (the body-only page as authored in Claude Code) into index.html."""
import pathlib
src = pathlib.Path(__file__).with_name('src-artifact.html').read_text()
title_end = src.index('</title>') + len('</title>')
head, rest = src[:title_end], src[title_end:]
style_end = rest.index('</style>') + len('</style>')
styles, body = rest[:style_end], rest[style_end:]
assert body.count('</script>') == 1
body = body.replace('</script>', '''
// ---- installable app: offline shell
if ('serviceWorker' in navigator && location.protocol === 'https:') {
  window.addEventListener('load', () => { navigator.serviceWorker.register('/sw.js').catch(() => {}); });
}
</script>''')
out = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#0c0a09">
<meta name="description" content="A physics-simulated kaleidoscope. Turn the phone and the glass tumbles; point it at light; or look through the camera as a teleidoscope.">
<link rel="manifest" href="/manifest.webmanifest">
<link rel="icon" type="image/svg+xml" href="/icon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="/icon-192.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black">
<meta property="og:title" content="Brass Kaleidoscope">
<meta property="og:description" content="Turn your phone and the glass tumbles. A kaleidoscope you can point at the light.">
<meta property="og:image" content="https://kaleidoscope.clockerly.com/icon-512.png">
{head}{styles}
<style>
  img{{max-width:100%}} [hidden]{{display:none!important}}
</style>
</head>
<body>{body}
</body>
</html>
'''
pathlib.Path(__file__).with_name('index.html').write_text(out)
print('index.html written', len(out), 'bytes')
