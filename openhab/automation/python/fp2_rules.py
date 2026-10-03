from openhab import rule
from openhab.triggers import ItemStateChangeTrigger
from org.slf4j import LoggerFactory

log = LoggerFactory.getLogger("org.openhab.rules.FP2Python")

@rule(
    name="FP2 Python Couch Automation",
    description="Python 3 binding rule for handling FP2 couch presence",
    triggers=[
        ItemStateChangeTrigger("swLivingRoomCouch", state="ON")
    ]
)
class FP2PythonCouchRule:
    def execute(self, module, inputs):
        log.info("Python Rule: Couch occupancy detected!")
        item_registry = inputs.get("itemRegistry") # or use standard scoping helpers depending on OH version
        # Example logic execution via command
        events.sendCommand("CouchLicht_Switch", "ON")
