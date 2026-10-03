const { rules, triggers, items, log } = require('openhab');

rules.JSRule({
  name: "FP2 JavaScript Couch Rule",
  description: "Turns on light when couch zone becomes active via JS scripting",
  triggers: [
    triggers.ItemStateChangeTrigger('swLivingRoomCouch', 'OFF', 'ON')
  ],
  execute: (event) => {
    log.info("JS Rule: Couch occupied!");
    let lux = items.getItem('numLivingRoomLux').numericState;
    if (lux < 150) {
      items.getItem('CouchLicht_Switch').sendCommand('ON');
    }
  }
});
