{
    "name": "MTS Connector",
    "category": "MTS",
    "version": "15.0.0.0.1",
    "sequence": 1,
    "author": "OpenG2P",
    "website": "https://github.com/OpenG2P/openg2p-mts",
    "license": "Other OSI approved licence",
    "depends": ["base", "queue_job"],
    "external_dependencies": {"python": ["pyjq"]},
    "data": [
        "security/ir.model.access.csv",
        "security/security.xml",
        "views/menuitems.xml",
        "views/mts_connector.xml",
    ],
    "assets": {},
    "demo": [],
    "images": [],
    "application": True,
    "installable": True,
    "auto_install": False,
}
