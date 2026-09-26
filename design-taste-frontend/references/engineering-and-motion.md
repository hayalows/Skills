# Engineering and motion

## Respect the project

Inspect dependencies and installed versions before importing libraries. Use the existing package manager. Check current official documentation for version-sensitive APIs. Keep interactive state in the framework’s supported client boundary; do not add client boundaries to every static component by habit.

Prefer semantic HTML and native CSS for simple layouts and interactions. Use Grid or Flexbox according to the content. Choose viewport units deliberately: stable and dynamic viewport heights serve different needs. Do not force every hero to full height.

## Animation choices

| Need | Prefer first | Verify |
| --- | --- | --- |
| Button feedback or disclosure | CSS or native transition | Focus parity and no layout shift |
| Element enters view | IntersectionObserver or supported CSS | Content remains accessible if animation fails |
| Existing React motion system | Its supported APIs | Installed version and reduced-motion path |
| Scroll storytelling | Purpose-built, isolated implementation | Escape, keyboard access, resize and mobile fallback |
| 3D product explanation | A justified canvas implementation | Accessible alternative and loading cost |

Avoid React state updates on every pointer or scroll frame. Use the animation system’s values, CSS or frame-batched DOM work. A passive scroll listener is not inherently broken, but unbounded per-frame work is a risk. Prefer transform and opacity for movement; measure costly layout animation when a real interaction needs it.

Do not let two libraries animate the same property on the same element. Multiple libraries can coexist when ownership is explicit, but check bundle cost before adding one. Clean up listeners, observers and animation contexts on unmount. Recompute dimensions when content or the viewport changes. Use stable item keys and avoid stale closures.

For pinned or horizontal sequences, keep a natural vertical fallback, avoid negative travel distances, account for container width and content changes, and test focus and reading order. Do not copy a skeleton and assume it works with arbitrary content.

## Accessibility and resilience

Respect reduced motion regardless of an internal motion score. Keep text visible and controls usable when animation is disabled. Provide pause controls for relevant automatic movement. Never make hover, dragging, color or animation the sole way to understand or operate something.

Use actual contrast measurements and appropriate current standards. Do not treat an 18 CSS-pixel label as automatically qualifying for a large-text exception. Include labels, help and error relationships in the accessibility tree. Test zoom, text reflow, keyboard paths and narrow screens.

For translucent surfaces, provide a legible solid fallback and check text against realistic backgrounds. Do not rely on blur or browser support for reduced-transparency media queries to make text readable. Describe a custom glass treatment as an independent web effect, not an official Apple component.

## Performance and completion

Reserve image and embed dimensions. Compress assets, load secondary media on demand and avoid delaying the main content behind animation. Inspect font fallback and loading behavior. Avoid making a small interaction depend on a large library without a clear benefit.

Use performance tools only when available and relevant. Record the tested page, device profile, network conditions and measurement type. Distinguish lab diagnostics from field-user results. Never report that a performance target was met without measurements.
