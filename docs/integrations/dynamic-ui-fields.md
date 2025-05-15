# Dynamic UI and Parameter Management for Integrations

This guide outlines new features for integrations: controlling parameter order, the `engine_placeholder` field (type 23), and the `triggers` section. These enhancements improve user experience and enable more dynamic configuration.

## 1. Parameter Order Control

The order of parameters in the YAML file determines their display order in the user interface. This applies to standard parameters only; built-in parameters, such as `Log Level` and the `Do Not Use by Default` checkbox ,and other system parameters, are static and cannot be repositioned. An exception is made for the `engine` dropdown, as detailed below.

## 2. Specifying Engine Location (Type 23)

The `engine` dropdown's location in the user interface is now explicitly defined using the `engine_placeholder` field (type 23). This replaces the previous implicit handling.  Built-in parameters such as `log_level` remain static and cannot be repositioned.  Positioning the `engine` dropdown is achieved by placing the `engine_placeholder` within the YAML configuration.  The `engine` dropdown then appears at the `engine_placeholder`'s location.

**YAML Structure:**

```yaml
- name: engine_placeholder
  type: 23
  section: Connect
```

**Important Note:** This functionality requires a compatible UI version.  Using `engine_placeholder` in an outdated UI will create a non-functional parameter with the name `engine_placeholder`.


## 3. Implementing Dynamic Behavior with Triggers
The `triggers` section enables dynamic UI behavior based on user input and enables you to define conditions and effects to control the visibility (`hidden`) and required status (`required`) of UI elements.

**YAML Structure:**

```yaml
triggers:
  - conditions:
      - name: <field_to_check> # Field whose value determines the effect
        operator: <operator>   # (exists, not_exists, equals, not_equals)
        value: <value>         # Value to compare against (required only for equals/not_equals)
    effects:
      - name: <field_to_affect> # Field whose properties are modified
        action:
          required: <true/false> # Set to true to make the field required, false otherwise
          required: true       # Makes the field mandatory if the condition is met
          # hidden: <true/false>  Can also be used here to hide/show the field.
          # Other UI actions are also possible.
```

**Example:** Hide the `token` field if the `username` field has a value:

```yaml
triggers:
  - conditions:
      - name: username
        operator: exists
    effects:
      - name: token
        action:
          hidden: true
```

The example demonstrates how to dynamically hide UI elements based on the existence of a username.  This prevents unnecessary display of the token field and avoids confusion.

**Note:** Multiple conditions within a trigger use an "AND" relationship; all conditions must be true for the effect to apply.



For a complete example, see the generic webhook integration.
