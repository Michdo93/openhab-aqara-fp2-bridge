# OpenHAB Aqara FP2 Bridge

This repository provides a complete configuration guide and file layout to integrate the **Aqara Presence Sensor FP2** into **openHAB** via **Home Assistant (MQTT)**. Since the FP2 lacks a native local API, Home Assistant acts as a local bridge utilizing HomeKit, forwarding data downstream via MQTT to openHAB.

---

## Architecture Overview


```
[ Aqara FP2 ] ---> (Wi-Fi / HomeKit) ---> [ Home Assistant VM ]
│
(MQTT Publish via Automations)
▼
[ MQTT Broker ]
│
(MQTT Binding)
▼
[ openHAB Engine ]
┌──────────────────────────┬───────────────┴───────────────┬──────────────────────────┐
▼                          ▼                               ▼                          ▼
[ .things / .items ]      [ .sitemaps ]               [ Rules: Rules DSL ]       [ Rules: JS / Python ]
```

---

## Step 1: Home Assistant Setup

1. **Pairing**: Pair your Aqara FP2 using the Aqara Home App to set up your tracking zones.
2. **Apple Home Removal**: If paired to Apple HomeKit, remove it (it can only connect to one controller natively via HomeKit protocol).
3. **Integration**: In Home Assistant, go to **Settings > Devices & Services** and add the FP2 via the **HomeKit Device Integration** using the 8-digit pairing code found on the device.
4. **MQTT Export**: Set up MQTT automations in Home Assistant so that every state change of your FP2 zones and sensors gets published to an MQTT broker (Mosquitto). Reference file: `home-assistant/mqtt_automations_example.yaml`.

---

## Step 2: openHAB Installation & File Deployment

Copy the files from this repository directly into your openHAB configuration directories (typically located under `/etc/openhab/` on Linux installations):

- Copy `things/fp2.things` $\rightarrow$ `/etc/openhab/things/fp2.things`
- Copy `items/fp2.items` $\rightarrow$ `/etc/openhab/items/fp2.items`
- Copy `sitemaps/fp2.sitemap` $\rightarrow$ `/etc/openhab/sitemaps/fp2.sitemap`
- Copy `rules/fp2_dsl.rules` $\rightarrow$ `/etc/openhab/rules/fp2_dsl.rules`
- Copy `automation/js/fp2_rules.js` $\rightarrow$ `/etc/openhab/automation/js/fp2_rules.js` *(Requires JS Scripting Add-on)*
- Copy `automation/python/fp2_rules.py` $\rightarrow$ `/etc/openhab/automation/python/fp2_rules.py` *(Requires Python Scripting Add-on)*

---

## Requirements

* openHAB 4.x / 5.x
* MQTT Binding & Mosquitto MQTT Broker configured
* JS Scripting Add-on (for JavaScript rules)
* Python Scripting Add-on / GraalPy (for Python 3 rules)

---
