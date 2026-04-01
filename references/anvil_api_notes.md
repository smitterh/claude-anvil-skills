# Anvil API Notes — Confirmed Patterns and Known Non-Existent APIs

## Dialogs / User Input

### `anvil.prompt()` — DOES NOT EXIST
There is no `anvil.prompt()` function. Do not use it.

### Correct pattern: `alert()` with a component
To ask the user for text input, pass a `TextBox` (or any component/form) to `alert()`:

```python
tb = TextBox(placeholder="e.g. 123 Main St")
confirmed = alert(tb, title="New BPO", buttons=[("Create", True), ("Cancel", False)])
if not confirmed:
    return
name = (tb.text or "").strip()
```

`alert()` is imported via `from anvil import *`. It returns the value of the chosen button.
To open a form as a popup, pass a form instance instead of a component:

```python
result = alert(MyForm(), large=True)
```

Reference: https://anvil.works/learn/tutorials/database-backed-apps/chapter-6#step-set-popup-content

### `Notification`
```python
Notification("Message here.", timeout=3).show()
```
Imported via `from anvil import *`. Displays a transient toast notification.

---

## Data Tables — Sorting

### Multiple `order_by` columns — use Python sort instead
Passing multiple `tables.order_by()` to `search()` has unverified behavior. Safe pattern:
```python
rows = app_tables.my_table.search(filter_col=value)
return sorted(rows, key=lambda r: (r['col1'], r['col2']))
```

---

## Data Tables — Transactions

### `tables.in_transaction` — DECORATOR ONLY, not a context manager
`with tables.in_transaction:` raises `AttributeError: __enter__`. Use it as a decorator on a nested function instead:

```python
@tables.in_transaction
def _do_work():
    app_tables.foo.add_row(...)
    app_tables.bar.add_row(...)
    return result

return _do_work()
```

To return a value from the transaction, return it inside `_do_work()` and capture it from the call.

---

## Navigation

### `open_form(form_name, **kwargs)`
Navigate to a top-level form:
```python
open_form('HomeForm')
open_form('EditBpoForm', report=report_row)
```
kwargs are passed as constructor arguments to the target form's `__init__`.

### `get_open_form()` — call parent form from a sub-component
`self.parent.parent` is FRAGILE — the depth varies depending on the layout (SaaS Starter wraps content in extra ColumnPanels). Use `get_open_form()` instead:

```python
# In a RepeatingPanel item template or sub-form:
get_open_form().refresh_list()   # calls method on the top-level form
```

`get_open_form()` is imported via `from anvil import *`. It always returns the current top-level form regardless of nesting depth.

---

## Server Calls

```python
result = anvil.server.call('function_name', arg1, arg2, keyword=value)
```

---

## Users

```python
user = anvil.users.get_user()   # returns current user row or None
anvil.users.logout()
anvil.users.login_with_form(allow_cancel=True, show_signup_option=True)
```

---

## Google Maps (`anvil.googlemaps.GoogleMap`)

Requires: **Google API Service integration** enabled in Anvil app settings (sets the API key — it is NOT a YAML property). All configuration is done in Python.

```python
from anvil.googlemaps import GoogleMap

# Basic map setup
map = GoogleMap()
map.center = GoogleMap.LatLng(lat, lng)
map.zoom = 13

# Marker
marker = GoogleMap.Marker(
    position=GoogleMap.LatLng(lat, lng),
    animation=GoogleMap.Animation.DROP,  # or .BOUNCE
    label="A"
)
map.add_component(marker)
marker.add_event_handler("click", handler_fn)

# InfoWindow (popup)
info = GoogleMap.InfoWindow(content="<b>Hello</b>")
info.open(map, marker)

# Polyline
line = GoogleMap.Polyline(
    path=[GoogleMap.LatLng(a, b), GoogleMap.LatLng(c, d)],
    stroke_color="#FF0000",
    stroke_weight=2
)
map.add_component(line)

# Geocoding (server or client)
results = GoogleMap.geocode(address="123 Main St, Tampa, FL")
# results[0].geometry.location → LatLng
# Reverse geocode:
results = GoogleMap.geocode(location=GoogleMap.LatLng(lat, lng))

# Utilities
GoogleMap.compute_length([latlng_list])   # distance in metres
GoogleMap.compute_area([polygon_vertices]) # area in m²
```

**Key points:**
- API key is configured via Anvil app settings → Services → Google API (not in YAML)
- `center` and `zoom` are set in Python, not YAML
- Events use `add_event_handler("click", fn)` on map or any overlay
- `map_type` may be settable in Python but is not documented
- For geocoding from server code, use the same `GoogleMap.geocode()` call

---

## Dependency Library

URL: https://dependency-library.anvil.app/ (Anvil runtime URL — must be viewed in browser, not fetchable programmatically)

This page lists community-built Anvil dependency packages that can be added to any Anvil app via their dependency ID (`dep_XXXXXXXX`). To use a dependency:
1. Open the page in browser, find the package
2. Copy its dependency ID or clone link
3. In Anvil editor: Settings → Dependencies → paste the ID

The BPO Generator 2.0 already uses `dep_gqlhr7sei7ys7` (Anvil SaaS Starter component library: NavigationDrawerLayout, NavigationLink, Card, Button M3, Text, etc.)
