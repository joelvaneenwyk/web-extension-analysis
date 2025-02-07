definitions = {
    "retire-example": {
        "vulnerabilities": [
            {
                "below": "0.0.2",
                "severity": "low",
                "identifiers": {
                    "CVE": ["CVE-XXXX-XXXX"],
                    "bug": "1234",
                    "summary": "bug summary",
                },
                "info": ["http://github.com/eoftedal/retire.js/"],
            }
        ],
        "extractors": {
            "func": ["retire.VERSION"],
            "filename": [r"retire-example-([0-9][0-9.a-z_-]+)(.min)?\.js"],
            "filecontent": [r"/\*!? Retire-example v([0-9][0-9.a-z_-]+)"],
            "hashes": {"07f8b94c8d601a24a1914a1a92bec0e4fafda964": "0.0.1"},
        },
    },
    "jquery": {
        "bowername": ["jQuery"],
        "vulnerabilities": [
            {
                "below": "1.6.3",
                "severity": "medium",
                "identifiers": {
                    "CVE": ["CVE-2011-4969"],
                    "summary": "XSS with location.hash",
                },
                "info": [
                    "https://nvd.nist.gov/vuln/detail/CVE-2011-4969",
                    "http://research.insecurelabs.org/jquery/test/",
                    "https://bugs.jquery.com/ticket/9521",
                ],
            },
            {
                "below": "1.9.0b1",
                "identifiers": {
                    "CVE": ["CVE-2012-6708"],
                    "bug": "11290",
                    "summary": "Selector interpreted as HTML",
                },
                "severity": "medium",
                "info": [
                    "http://bugs.jquery.com/ticket/11290",
                    "https://nvd.nist.gov/vuln/detail/CVE-2012-6708",
                    "http://research.insecurelabs.org/jquery/test/",
                ],
            },
            {
                "atOrAbove": "1.4.0",
                "below": "1.12.0",
                "identifiers": {
                    "issue": "2432",
                    "summary": "3rd party CORS request may execute",
                    "CVE": ["CVE-2015-9251"],
                },
                "severity": "medium",
                "info": [
                    "https://github.com/jquery/jquery/issues/2432",
                    "http://blog.jquery.com/2016/01/08/jquery-2-2-and-1-12-released/",
                    "https://nvd.nist.gov/vuln/detail/CVE-2015-9251",
                    "http://research.insecurelabs.org/jquery/test/",
                ],
            },
            {
                "atOrAbove": "1.12.3",
                "below": "3.0.0-beta1",
                "identifiers": {
                    "issue": "2432",
                    "summary": "3rd party CORS request may execute",
                    "CVE": ["CVE-2015-9251"],
                },
                "severity": "medium",
                "info": [
                    "https://github.com/jquery/jquery/issues/2432",
                    "http://blog.jquery.com/2016/01/08/jquery-2-2-and-1-12-released/",
                    "https://nvd.nist.gov/vuln/detail/CVE-2015-9251",
                    "http://research.insecurelabs.org/jquery/test/",
                ],
            },
            {
                "atOrAbove": "1.8.0",
                "below": "1.12.0",
                "identifiers": {
                    "CVE": ["CVE-2015-9251"],
                    "issue": "11974",
                    "summary": "parseHTML() executes scripts in event handlers",
                },
                "severity": "medium",
                "info": [
                    "https://bugs.jquery.com/ticket/11974",
                    "https://nvd.nist.gov/vuln/detail/CVE-2015-9251",
                    "http://research.insecurelabs.org/jquery/test/",
                ],
            },
            {
                "atOrAbove": "1.12.2",
                "below": "2.2.0",
                "identifiers": {
                    "CVE": ["CVE-2015-9251"],
                    "issue": "11974",
                    "summary": "parseHTML() executes scripts in event handlers",
                },
                "severity": "medium",
                "info": [
                    "https://bugs.jquery.com/ticket/11974",
                    "https://nvd.nist.gov/vuln/detail/CVE-2015-9251",
                    "http://research.insecurelabs.org/jquery/test/",
                ],
            },
            {
                "atOrAbove": "2.2.2",
                "below": "3.0.0",
                "identifiers": {
                    "CVE": ["CVE-2015-9251"],
                    "issue": "11974",
                    "summary": "parseHTML() executes scripts in event handlers",
                },
                "severity": "medium",
                "info": [
                    "https://bugs.jquery.com/ticket/11974",
                    "https://nvd.nist.gov/vuln/detail/CVE-2015-9251",
                    "http://research.insecurelabs.org/jquery/test/",
                ],
            },
            {
                "below": "3.4.0",
                "identifiers": {
                    "CVE": ["CVE-2019-11358"],
                    "summary": "jQuery before 3.4.0, as used in Drupal, Backdrop CMS, and other products, mishandles jQuery.extend(true, {}, ...) because of Object.prototype pollution",
                },
                "severity": "low",
                "info": [
                    "https://blog.jquery.com/2019/04/10/jquery-3-4-0-released/",
                    "https://nvd.nist.gov/vuln/detail/CVE-2019-11358",
                    "https://github.com/jquery/jquery/commit/753d591aea698e57d6db58c9f722cd0808619b1b",
                ],
            },
        ],
        "extractors": {
            "func": [
                "(jQuery || $ || $jq || $j).fn.jquery",
                "require('jquery').fn.jquery",
            ],
            "uri": [r"/([0-9][0-9.a-z_-]+)/jquery(\.min)?\.js"],
            "filename": [r"jquery-([0-9][0-9.a-z_-]+)(\.min)?\.js"],
            "filecontent": [
                r"/\*!? jQuery v([0-9][0-9.a-z_-]+)",
                r"\* jQuery JavaScript Library v([0-9][0-9.a-z_-]+)",
                r"\* jQuery ([0-9][0-9.a-z_-]+) - New Wave Javascript",
                r"// \$Id: jquery.js,v ([0-9][0-9.a-z_-]+)",
                r"/\*! jQuery v([0-9][0-9.a-z_-]+)",
                r'[^a-z]f="([0-9][0-9.a-z_-]+)",.*[^a-z]jquery:f,',
                r'[^a-z]m="([0-9][0-9.a-z_-]+)",.*[^a-z]jquery:m,',
                r'[^a-z.]jquery:[ ]?"([0-9][0-9.a-z_-]+)"',
                r'\$\.documentElement,Q=e.jQuery,Z=e\.\$,ee=\{\},te=\[\],ne="([0-9][0-9.a-z_-]+)"',
            ],
            "filecontentreplace": [
                r'/var [a-z]=[a-z]\.document,([a-z])="([0-9][0-9.a-z_-]+)",([a-z])=.{130,160};\3\.fn=\3\.prototype=\{jquery:\1/$2/'
            ],
            "hashes": {},
        },
    },
    "jquery-migrate": {
        "vulnerabilities": [
            {
                "below": "1.2.0",
                "severity": "medium",
                "identifiers": {
                    "release": "jQuery Migrate 1.2.0 Released",
                    "summary": "cross-site-scripting",
                },
                "info": [
                    "http://blog.jquery.com/2013/05/01/jquery-migrate-1-2-0-released/"
                ],
            },
            {
                "below": "1.2.2",
                "severity": "medium",
                "identifiers": {
                    "bug": "11290",
                    "summary": "Selector interpreted as HTML",
                },
                "info": [
                    "http://bugs.jquery.com/ticket/11290",
                    "http://research.insecurelabs.org/jquery/test/",
                ],
            },
        ],
        "extractors": {
            "filename": [r"jquery-migrate-([0-9][0-9.a-z_-]+)(.min)?\.js"],
            "filecontent": [
                r"/\*!?(?:\n \*)? jQuery Migrate(?: -)? v([0-9][0-9.a-z_-]+)"
            ],
            "hashes": {},
        },
    },
    "jquery.validator": {
        "bowername": ["jquery-validator"],
        "vulnerabilities": [],
        "extractors": {
            "func": ["jQuery.validation.version"],
            "filename": [r"jquery.validation-([0-9][0-9.a-z_-]+)(.min)?\.js"],
            "uri": [r"/([0-9][0-9.a-z_-]+)/jquery.validation(\.min)?\.js"],
            "filecontent": [
                r"/\*!?(?:\n \*)? jQuery Validation Plugin v([0-9][0-9.a-z_-]+)"
            ],
            "hashes": {},
        },
    },
    "jquery-mobile": {
        "bowername": [
            "jquery-mobile",
            "jquery-mobile-min",
            "jquery-mobile-build",
            "jquery-mobile-dist",
            "jquery-mobile-bower",
        ],
        "vulnerabilities": [
            {
                "below": "1.0RC2",
                "severity": "high",
                "identifiers": {"osvdb": ["94563", "93562", "94316", "94561", "94560"]},
                "info": [
                    "http://osvdb.org/show/osvdb/94563",
                    "http://osvdb.org/show/osvdb/94562",
                    "http://osvdb.org/show/osvdb/94316",
                    "http://osvdb.org/show/osvdb/94561",
                    "http://osvdb.org/show/osvdb/94560",
                ],
            },
            {
                "below": "1.0.1",
                "severity": "high",
                "identifiers": {"osvdb": ["94317"]},
                "info": ["http://osvdb.org/show/osvdb/94317"],
            },
            {
                "below": "1.1.2",
                "severity": "medium",
                "identifiers": {
                    "issue": "4787",
                    "release": "http://jquerymobile.com/changelog/1.1.2/",
                    "summary": "location.href cross-site scripting",
                },
                "info": [
                    "http://jquerymobile.com/changelog/1.1.2/",
                    "https://github.com/jquery/jquery-mobile/issues/4787",
                ],
            },
            {
                "below": "1.2.0",
                "severity": "medium",
                "identifiers": {
                    "issue": "4787",
                    "release": "http://jquerymobile.com/changelog/1.2.0/",
                    "summary": "location.href cross-site scripting",
                },
                "info": [
                    "http://jquerymobile.com/changelog/1.2.0/",
                    "https://github.com/jquery/jquery-mobile/issues/4787",
                ],
            },
            {
                "below": "100.0.0",
                "severity": "medium",
                "identifiers": {
                    "summary": "open redirect leads to cross site scripting"
                },
                "info": [
                    "http://sirdarckcat.blogspot.no/2017/02/unpatched-0day-jquery-mobile-xss.html"
                ],
            },
        ],
        "extractors": {
            "func": ["jQuery.mobile.version"],
            "filename": [r"jquery.mobile-([0-9][0-9.a-z_-]+)(.min)?\.js"],
            "uri": [r"/([0-9][0-9.a-z_-]+)/jquery.mobile(\.min)?\.js"],
            "filecontent": [
                r"/\*!?(?:\n \*)? jQuery Mobile(?: -)? v([0-9][0-9.a-z_-]+)"
            ],
            "hashes": {},
        },
    },
    "jquery-ui-dialog": {
        "bowername": ["jquery-ui", "jquery.ui"],
        "vulnerabilities": [
            {
                "atOrAbove": "1.8.9",
                "below": "1.10.0",
                "severity": "medium",
                "identifiers": {
                    "CVE": ["CVE-2010-5312"],
                    "bug": "6016",
                    "summary": "Title cross-site scripting vulnerability",
                },
                "info": [
                    "http://bugs.jqueryui.com/ticket/6016",
                    "https://nvd.nist.gov/vuln/detail/CVE-2010-5312",
                ],
            },
            {
                "below": "1.12.0",
                "severity": "high",
                "identifiers": {
                    "CVE": ["CVE-2016-7103"],
                    "bug": "281",
                    "summary": "XSS Vulnerability on closeText option",
                },
                "info": [
                    "https://github.com/jquery/api.jqueryui.com/issues/281",
                    "https://nvd.nist.gov/vuln/detail/CVE-2016-7103",
                    "https://snyk.io/vuln/npm:jquery-ui:20160721",
                ],
            },
        ],
        "extractors": {
            "func": ["jQuery.ui.dialog.version"],
            "filecontent": [
                r"/\*!? jQuery UI - v([0-9][0-9.a-z_-]+)(.*\n){1,3}.*jquery\.ui\.dialog\.js",
                r"/\*!?[\n *]+jQuery UI ([0-9][0-9.a-z_-]+)(.*\n)*.*\.ui\.dialog",
                r"/\*!?[\n *]+jQuery UI Dialog ([0-9][0-9.a-z_-]+)",
                r"/\*!? jQuery UI - v([0-9][0-9.a-z_-]+)(.*\n){1,3}\* Includes: .* dialog\.js",
            ],
            "hashes": {},
        },
    },
    "jquery-ui-autocomplete": {
        "bowername": ["jquery-ui", "jquery.ui"],
        "vulnerabilities": [],
        "extractors": {
            "func": ["jQuery.ui.autocomplete.version"],
            "filecontent": [
                r"/\*!? jQuery UI - v([0-9][0-9.a-z_-]+)(.*\n){1,3}.*jquery\.ui\.autocomplete\.js",
                r"/\*!?[\n *]+jQuery UI ([0-9][0-9.a-z_-]+)(.*\n)*.*\.ui\.autocomplete",
                r"/\*!?[\n *]+jQuery UI Autocomplete ([0-9][0-9.a-z_-]+)",
                r"/\*!? jQuery UI - v([0-9][0-9.a-z_-]+)(.*\n){1,3}\* Includes: .* autocomplete\.js",
            ],
            "hashes": {},
        },
    },
    "jquery-ui-tooltip": {
        "bowername": ["jquery-ui", "jquery.ui"],
        "vulnerabilities": [
            {
                "atOrAbove": "1.9.2",
                "below": "1.10.0",
                "severity": "high",
                "identifiers": {
                    "CVE": ["CVE-2012-6662"],
                    "bug": "8859",
                    "summary": "Autocomplete cross-site scripting vulnerability",
                },
                "info": [
                    "http://bugs.jqueryui.com/ticket/8859",
                    "https://nvd.nist.gov/vuln/detail/CVE-2012-6662",
                ],
            }
        ],
        "extractors": {
            "func": ["jQuery.ui.tooltip.version"],
            "filecontent": [
                r"/\*!? jQuery UI - v([0-9][0-9.a-z_-]+)(.*\n){1,3}.*jquery\.ui\.tooltip\.js",
                r"/\*!?[\n *]+jQuery UI ([0-9][0-9.a-z_-]+)(.*\n)*.*\.ui\.tooltip",
                r"/\*!?[\n *]+jQuery UI Tooltip ([0-9][0-9.a-z_-]+)",
            ],
            "hashes": {},
        },
    },
    "jquery.prettyPhoto": {
        "bowername": ["jquery-prettyPhoto"],
        "vulnerabilities": [
            {
                "below": "3.1.5",
                "severity": "high",
                "identifiers": {"CVE": ["CVE-2013-6837"]},
                "info": ["https://nvd.nist.gov/vuln/detail/CVE-2013-6837"],
            },
            {
                "below": "3.1.6",
                "severity": "high",
                "info": [
                    "https://github.com/scaron/prettyphoto/issues/149",
                    "https://blog.anantshri.info/forgotten_disclosure_dom_xss_prettyphoto",
                ],
            },
        ],
        "extractors": {
            "func": ["jQuery.prettyPhoto.version"],
            "filecontent": [
                r"/\*(?:.*[\n\r]+){1,3}.*Class: prettyPhoto(?:.*[\n\r]+){1,3}.*Version: ([0-9][0-9.a-z_-]+)",
                r"\.prettyPhoto[ ]?=[ ]?\{version:[ ]?(?:'|\")([0-9][0-9.a-z_-]+)(?:'|\")\}",
            ],
            "hashes": {},
        },
    },
    "jPlayer": {
        "bowername": ["jPlayer"],
        "vulnerabilities": [
            {
                "below": "2.3.1",
                "severity": "high",
                "identifiers": {
                    "CVE": ["CVE-2013-2023"],
                    "release": "2.3.1",
                    "summary": "XSS vulnerability in actionscript/Jplayer.as in the Flash SWF component",
                },
                "info": [
                    "http://jplayer.org/latest/release-notes/",
                    "https://nvd.nist.gov/vuln/detail/CVE-2013-2023",
                ],
            },
            {
                "below": "2.3.23",
                "severity": "high",
                "identifiers": {
                    "CVE": ["CVE-2013-2022"],
                    "release": "2.3.23",
                    "summary": "XSS vulnerabilities in actionscript/Jplayer.as in the Flash SWF component",
                },
                "info": [
                    "http://jplayer.org/latest/release-notes/",
                    "https://nvd.nist.gov/vuln/detail/CVE-2013-2022",
                ],
            },
            {
                "below": "2.2.20",
                "severity": "high",
                "identifiers": {
                    "CVE": ["CVE-2013-1942"],
                    "release": "2.2.20",
                    "summary": "XSS vulnerabilities in actionscript/Jplayer.as in the Flash SWF component",
                },
                "info": [
                    "http://jplayer.org/latest/release-notes/",
                    "https://nvd.nist.gov/vuln/detail/CVE-2013-1942",
                ],
            },
        ],
        "extractors": {
            "func": ["new jQuery.jPlayer().version.script"],
            "filecontent": [
                r"/\*(?:.*[\n\r]+){1,3}.*jPlayer Plugin for jQuery(?:.*[\n\r]+){1,10}.*Version: ([0-9][0-9.a-z_-]+)"
            ],
            "hashes": {},
        },
    },
    "knockout": {
        "vulnerabilities": [
            {
                "below": "3.5.0-beta",
                "severity": "medium",
                "identifiers": {
                    "summary": "XSS injection point in attr name binding for browser IE7 and older"
                },
                "info": ["https://github.com/knockout/knockout/issues/1244"],
            }
        ],
        "extractors": {
            "func": ["ko.version"],
            "filename": [r"knockout-([0-9][0-9.a-z_-]+)(.min)?\.js"],
            "filecontent": [r"\* Knockout JavaScript library v([0-9][0-9.a-z_-]+)"],
            "hashes": {},
        },
    },
    "sessvars": {
        "vulnerabilities": [
            {
                "below": "1.01",
                "severity": "low",
                "identifiers": {"summary": "Unsanitized data passed to eval()"},
                "info": ["http://www.thomasfrank.se/sessionvars.html"],
            }
        ],
        "extractors": {
            "filename": [r"sessvars-([0-9][0-9.a-z_-]+)(.min)?\.js"],
            "filecontent": [r"sessvars ver ([0-9][0-9.a-z_-]+)"],
            "hashes": {},
        },
    },
    "swfobject": {
        "bowername": ["swfobject", "swfobject-bower"],
        "vulnerabilities": [
            {
                "below": "2.1",
                "severity": "medium",
                "identifiers": {"summary": "DOM-based XSS"},
                "info": [
                    "https://github.com/swfobject/swfobject/wiki/SWFObject-Release-Notes#swfobject-v21-beta7-june-6th-2008"
                ],
            }
        ],
        "extractors": {
            "filename": [r"swfobject_([0-9][0-9.a-z_-]+)(.min)?\.js"],
            "filecontent": [r"SWFObject v([0-9][0-9.a-z_-]+) "],
            "hashes": {},
        },
    },
    "tinyMCE": {
        "bowername": ["tinymce", "tinymce-dist"],
        "vulnerabilities": [
            {
                "below": "1.4.2",
                "severity": "high",
                "identifiers": {
                    "summary": "Static code injection vulnerability in inc/function.base.php",
                    "CVE": ["CVE-2011-4825"],
                },
                "info": ["http://www.cvedetails.com/cve/CVE-2011-4825/"],
            },
            {
                "below": "4.2.4",
                "severity": "medium",
                "identifiers": {
                    "summary": "xss issues with media plugin not properly filtering out some script attributes."
                },
                "info": ["https://www.tinymce.com/docs/changelog/"],
            },
            {
                "below": "4.2.0",
                "severity": "medium",
                "identifiers": {
                    "summary": "FIXED so script elements gets removed by default to prevent possible XSS issues in default config implementations"
                },
                "info": ["https://www.tinymce.com/docs/changelog/"],
            },
            {
                "below": "4.7.12",
                "severity": "medium",
                "identifiers": {
                    "summary": "FIXED so links with xlink:href attributes are filtered correctly to prevent XSS."
                },
                "info": ["https://www.tinymce.com/docs/changelog/"],
            },
        ],
        "extractors": {
            "filecontent": [
                r"// ([0-9][0-9.a-z_-]+) \([0-9\-]+\)[\n\r]+.{0,1200}l=.tinymce/geom/Rect."
            ],
            "filecontentreplace": [
                r"/tinyMCEPreInit.*majorVersion:.([0-9]+).,minorVersion:.([0-9.]+)./$1.$2/",
                r"/majorVersion:.([0-9]+).,minorVersion:.([0-9.]+).,.*tinyMCEPreInit/$1.$2/",
            ],
            "func": ["tinyMCE.majorVersion + '.'+ tinyMCE.minorVersion"],
        },
    },
    "YUI": {
        "bowername": ["yui", "yui3"],
        "vulnerabilities": [
            {
                "atOrAbove": "3.5.0",
                "below": "3.9.2",
                "severity": "high",
                "identifiers": {"CVE": ["CVE-2013-4942"]},
                "info": ["http://www.cvedetails.com/cve/CVE-2013-4942/"],
            },
            {
                "atOrAbove": "3.2.0",
                "below": "3.9.2",
                "severity": "high",
                "identifiers": {"CVE": ["CVE-2013-4941"]},
                "info": ["http://www.cvedetails.com/cve/CVE-2013-4941/"],
            },
            {
                "atOrAbove": "3.0.0",
                "below": "3.10.3",
                "severity": "high",
                "identifiers": {"CVE": ["CVE-2013-4940"]},
                "info": ["http://www.cvedetails.com/cve/CVE-2013-4940/"],
            },
            {
                "atOrAbove": "3.0.0",
                "below": "3.9.2",
                "severity": "high",
                "identifiers": {"CVE": ["CVE-2013-4939"]},
                "info": ["http://www.cvedetails.com/cve/CVE-2013-4939/"],
            },
            {
                "atOrAbove": "2.8.0",
                "below": "2.9.1",
                "severity": "high",
                "identifiers": {"CVE": ["CVE-2012-5883"]},
                "info": ["http://www.cvedetails.com/cve/CVE-2012-5883/"],
            },
            {
                "atOrAbove": "2.5.0",
                "below": "2.9.1",
                "severity": "high",
                "identifiers": {"CVE": ["CVE-2012-5882"]},
                "info": ["http://www.cvedetails.com/cve/CVE-2012-5882/"],
            },
            {
                "atOrAbove": "2.4.0",
                "below": "2.9.1",
                "severity": "high",
                "identifiers": {"CVE": ["CVE-2012-5881"]},
                "info": ["http://www.cvedetails.com/cve/CVE-2012-5881/"],
            },
            {
                "below": "2.9.0",
                "severity": "medium",
                "identifiers": {"CVE": ["CVE-2010-4710"]},
                "info": ["http://www.cvedetails.com/cve/CVE-2010-4710/"],
            },
            {
                "atOrAbove": "2.8.0",
                "below": "2.8.2",
                "severity": "high",
                "identifiers": {"CVE": ["CVE-2010-4209"]},
                "info": ["http://www.cvedetails.com/cve/CVE-2010-4209/"],
            },
            {
                "atOrAbove": "2.5.0",
                "below": "2.8.2",
                "severity": "high",
                "identifiers": {"CVE": ["CVE-2010-4208"]},
                "info": ["http://www.cvedetails.com/cve/CVE-2010-4208/"],
            },
            {
                "atOrAbove": "2.4.0",
                "below": "2.8.2",
                "severity": "high",
                "identifiers": {"CVE": ["CVE-2010-4207"]},
                "info": ["http://www.cvedetails.com/cve/CVE-2010-4207/"],
            },
        ],
        "extractors": {
            "func": ["YUI.Version", "YAHOO.VERSION"],
            "filename": [r"yui-([0-9][0-9.a-z_-]+)(.min)?\.js"],
            "filecontent": [
                r"/*\nYUI ([0-9][0-9.a-z_-]+)",
                r"/yui/license.(?:html|txt)\nversion: ([0-9][0-9.a-z_-]+)",
            ],
            "hashes": {},
        },
    },
    "prototypejs": {
        "bowername": ["prototypejs", "prototype.js", "prototypejs-bower"],
        "vulnerabilities": [
            {
                "atOrAbove": "1.6.0",
                "below": "1.6.0.2",
                "severity": "high",
                "identifiers": {"CVE": ["CVE-2008-7220"]},
                "info": [
                    "http://www.cvedetails.com/cve/CVE-2008-7220/",
                    "http://prototypejs.org/2008/01/25/prototype-1-6-0-2-bug-fixes-performance-improvements-and-security/",
                ],
            },
            {
                "below": "1.5.1.2",
                "severity": "high",
                "identifiers": {"CVE": ["CVE-2008-7220"]},
                "info": [
                    "http://www.cvedetails.com/cve/CVE-2008-7220/",
                    "http://prototypejs.org/2008/01/25/prototype-1-6-0-2-bug-fixes-performance-improvements-and-security/",
                ],
            },
        ],
        "extractors": {
            "func": ["Prototype.Version"],
            "uri": [r"/([0-9][0-9.a-z_-]+)/prototype(\.min)?\.js"],
            "filename": [r"prototype-([0-9][0-9.a-z_-]+)(.min)?\.js"],
            "filecontent": [
                r"Prototype JavaScript framework, version ([0-9][0-9.a-z_-]+)",
                r"Prototype[ ]?=[ ]?\{[ \r\n\t]*Version:[ ]?(?:'|\")([0-9][0-9.a-z_-]+)(?:'|\")",
            ],
            "hashes": {},
        },
    },
    "ember": {
        "vulnerabilities": [
            {
                "atOrAbove": "1.8.0",
                "below": "1.11.4",
                "severity": "medium",
                "identifiers": {"CVE": ["CVE-2015-7565"]},
                "info": [
                    "https://groups.google.com/forum/#!topic/ember-security/OfyQkoSuppY"
                ],
            },
            {
                "atOrAbove": "1.12.0",
                "below": "1.12.2",
                "severity": "medium",
                "identifiers": {"CVE": ["CVE-2015-7565"]},
                "info": [
                    "https://groups.google.com/forum/#!topic/ember-security/OfyQkoSuppY"
                ],
            },
            {
                "atOrAbove": "1.13.0",
                "below": "1.13.12",
                "severity": "medium",
                "identifiers": {"CVE": ["CVE-2015-7565"]},
                "info": [
                    "https://groups.google.com/forum/#!topic/ember-security/OfyQkoSuppY"
                ],
            },
            {
                "atOrAbove": "2.0.0",
                "below": "2.0.3",
                "severity": "medium",
                "identifiers": {"CVE": ["CVE-2015-7565"]},
                "info": [
                    "https://groups.google.com/forum/#!topic/ember-security/OfyQkoSuppY"
                ],
            },
            {
                "atOrAbove": "2.1.0",
                "below": "2.1.2",
                "severity": "medium",
                "identifiers": {"CVE": ["CVE-2015-7565"]},
                "info": [
                    "https://groups.google.com/forum/#!topic/ember-security/OfyQkoSuppY"
                ],
            },
            {
                "atOrAbove": "2.2.0",
                "below": "2.2.1",
                "severity": "medium",
                "identifiers": {"CVE": ["CVE-2015-7565"]},
                "info": [
                    "https://groups.google.com/forum/#!topic/ember-security/OfyQkoSuppY"
                ],
            },
            {
                "below": "1.5.0",
                "severity": "medium",
                "identifiers": {
                    "CVE": ["CVE-2014-0046"],
                    "summary": "ember-routing-auto-location can be forced to redirect to another domain",
                },
                "info": [
                    "https://github.com/emberjs/ember.js/blob/v1.5.0/CHANGELOG.md"
                ],
            },
            {
                "atOrAbove": "1.3.0-*",
                "below": "1.3.2",
                "severity": "medium",
                "identifiers": {"CVE": ["CVE-2014-0046"]},
                "info": [
                    "https://groups.google.com/forum/#!topic/ember-security/1h6FRgr8lXQ"
                ],
            },
            {
                "atOrAbove": "1.2.0-*",
                "below": "1.2.2",
                "severity": "medium",
                "identifiers": {"CVE": ["CVE-2014-0046"]},
                "info": [
                    "https://groups.google.com/forum/#!topic/ember-security/1h6FRgr8lXQ"
                ],
            },
            {
                "atOrAbove": "1.4.0-*",
                "below": "1.4.0-beta.2",
                "severity": "high",
                "identifiers": {"CVE": ["CVE-2014-0013", "CVE-2014-0014"]},
                "info": [
                    "https://groups.google.com/forum/#!topic/ember-security/2kpXXCxISS4",
                    "https://groups.google.com/forum/#!topic/ember-security/PSE4RzTi6l4",
                ],
            },
            {
                "atOrAbove": "1.3.0-*",
                "below": "1.3.1",
                "severity": "high",
                "identifiers": {"CVE": ["CVE-2014-0013", "CVE-2014-0014"]},
                "info": [
                    "https://groups.google.com/forum/#!topic/ember-security/2kpXXCxISS4",
                    "https://groups.google.com/forum/#!topic/ember-security/PSE4RzTi6l4",
                ],
            },
            {
                "atOrAbove": "1.2.0-*",
                "below": "1.2.1",
                "severity": "high",
                "identifiers": {"CVE": ["CVE-2014-0013", "CVE-2014-0014"]},
                "info": [
                    "https://groups.google.com/forum/#!topic/ember-security/2kpXXCxISS4",
                    "https://groups.google.com/forum/#!topic/ember-security/PSE4RzTi6l4",
                ],
            },
            {
                "atOrAbove": "1.1.0-*",
                "below": "1.1.3",
                "severity": "high",
                "identifiers": {"CVE": ["CVE-2014-0013", "CVE-2014-0014"]},
                "info": [
                    "https://groups.google.com/forum/#!topic/ember-security/2kpXXCxISS4",
                    "https://groups.google.com/forum/#!topic/ember-security/PSE4RzTi6l4",
                ],
            },
            {
                "atOrAbove": "1.0.0-*",
                "below": "1.0.1",
                "severity": "high",
                "identifiers": {"CVE": ["CVE-2014-0013", "CVE-2014-0014"]},
                "info": [
                    "https://groups.google.com/forum/#!topic/ember-security/2kpXXCxISS4",
                    "https://groups.google.com/forum/#!topic/ember-security/PSE4RzTi6l4",
                ],
            },
            {
                "atOrAbove": "1.0.0-rc.1",
                "below": "1.0.0-rc.1.1",
                "severity": "medium",
                "identifiers": {"CVE": ["CVE-2013-4170"]},
                "info": [
                    "https://groups.google.com/forum/#!topic/ember-security/dokLVwwxAdM"
                ],
            },
            {
                "atOrAbove": "1.0.0-rc.2",
                "below": "1.0.0-rc.2.1",
                "severity": "medium",
                "identifiers": {"CVE": ["CVE-2013-4170"]},
                "info": [
                    "https://groups.google.com/forum/#!topic/ember-security/dokLVwwxAdM"
                ],
            },
            {
                "atOrAbove": "1.0.0-rc.3",
                "below": "1.0.0-rc.3.1",
                "severity": "medium",
                "identifiers": {"CVE": ["CVE-2013-4170"]},
                "info": [
                    "https://groups.google.com/forum/#!topic/ember-security/dokLVwwxAdM"
                ],
            },
            {
                "atOrAbove": "1.0.0-rc.4",
                "below": "1.0.0-rc.4.1",
                "severity": "medium",
                "identifiers": {"CVE": ["CVE-2013-4170"]},
                "info": [
                    "https://groups.google.com/forum/#!topic/ember-security/dokLVwwxAdM"
                ],
            },
            {
                "atOrAbove": "1.0.0-rc.5",
                "below": "1.0.0-rc.5.1",
                "severity": "medium",
                "identifiers": {"CVE": ["CVE-2013-4170"]},
                "info": [
                    "https://groups.google.com/forum/#!topic/ember-security/dokLVwwxAdM"
                ],
            },
            {
                "atOrAbove": "1.0.0-rc.6",
                "below": "1.0.0-rc.6.1",
                "severity": "medium",
                "identifiers": {"CVE": ["CVE-2013-4170"]},
                "info": [
                    "https://groups.google.com/forum/#!topic/ember-security/dokLVwwxAdM"
                ],
            },
            {
                "below": "0.9.7.1",
                "info": ["https://github.com/emberjs/ember.js/blob/master/CHANGELOG"],
            },
            {
                "below": "0.9.7",
                "severity": "high",
                "identifiers": {
                    "bug": "699",
                    "summary": "Bound attributes aren't escaped properly",
                },
                "info": ["https://github.com/emberjs/ember.js/issues/699"],
            },
        ],
        "extractors": {
            "func": ["Ember.VERSION"],
            "uri": [r"/(?:v)?([0-9][0-9.a-z_-]+)/ember(\.min)?\.js"],
            "filename": [r"ember-([0-9][0-9.a-z_-]+)(\.min)?\.js"],
            "filecontent": [
                r"Project:   Ember -(?:.*\n){9,11}// Version: v([0-9][0-9.a-z_-]+)",
                r"// Version: v([0-9][0-9.a-z_-]+)(.*\n){10,15}(Ember Debug|@module ember|@class ember)",
                r"Ember.VERSION[ ]?=[ ]?(?:'|\")([0-9][0-9.a-z_-]+)(?:'|\")",
            ],
            "hashes": {},
        },
    },
    "dojo": {
        "vulnerabilities": [
            {
                "atOrAbove": "0.4",
                "below": "0.4.4",
                "severity": "high",
                "identifiers": {"CVE": ["CVE-2010-2276", "CVE-2010-2272"]},
                "info": [
                    "http://dojotoolkit.org/blog/dojo-security-advisory",
                    "http://www.cvedetails.com/cve/CVE-2010-2276/",
                    "http://www.cvedetails.com/cve/CVE-2010-2272/",
                ],
            },
            {
                "atOrAbove": "1.0",
                "below": "1.0.3",
                "severity": "high",
                "identifiers": {
                    "CVE": ["CVE-2010-2276", "CVE-2010-2274", "CVE-2010-2273"]
                },
                "info": [
                    "http://dojotoolkit.org/blog/dojo-security-advisory",
                    "http://www.cvedetails.com/cve/CVE-2010-2276/",
                    "http://www.cvedetails.com/cve/CVE-2010-2274/",
                    "http://www.cvedetails.com/cve/CVE-2010-2273/",
                ],
            },
            {
                "atOrAbove": "1.1",
                "below": "1.1.2",
                "severity": "high",
                "identifiers": {
                    "CVE": ["CVE-2010-2276", "CVE-2010-2274", "CVE-2010-2273"]
                },
                "info": [
                    "http://dojotoolkit.org/blog/dojo-security-advisory",
                    "http://www.cvedetails.com/cve/CVE-2010-2276/",
                    "http://www.cvedetails.com/cve/CVE-2010-2274/",
                    "http://www.cvedetails.com/cve/CVE-2010-2273/",
                ],
            },
            {
                "atOrAbove": "1.2",
                "below": "1.2.4",
                "severity": "high",
                "identifiers": {
                    "CVE": ["CVE-2010-2276", "CVE-2010-2274", "CVE-2010-2273"]
                },
                "info": [
                    "http://dojotoolkit.org/blog/dojo-security-advisory",
                    "http://www.cvedetails.com/cve/CVE-2010-2276/",
                    "http://www.cvedetails.com/cve/CVE-2010-2274/",
                    "http://www.cvedetails.com/cve/CVE-2010-2273/",
                ],
            },
            {
                "atOrAbove": "1.3",
                "below": "1.3.3",
                "severity": "high",
                "identifiers": {
                    "CVE": ["CVE-2010-2276", "CVE-2010-2274", "CVE-2010-2273"]
                },
                "info": [
                    "http://dojotoolkit.org/blog/dojo-security-advisory",
                    "http://www.cvedetails.com/cve/CVE-2010-2276/",
                    "http://www.cvedetails.com/cve/CVE-2010-2274/",
                    "http://www.cvedetails.com/cve/CVE-2010-2273/",
                ],
            },
            {
                "atOrAbove": "1.4",
                "below": "1.4.2",
                "severity": "high",
                "identifiers": {
                    "CVE": ["CVE-2010-2276", "CVE-2010-2274", "CVE-2010-2273"]
                },
                "info": [
                    "http://dojotoolkit.org/blog/dojo-security-advisory",
                    "http://www.cvedetails.com/cve/CVE-2010-2276/",
                    "http://www.cvedetails.com/cve/CVE-2010-2274/",
                    "http://www.cvedetails.com/cve/CVE-2010-2273/",
                ],
            },
            {
                "below": "1.4.2",
                "severity": "medium",
                "identifiers": {"CVE": ["CVE-2010-2275"]},
                "info": ["http://www.cvedetails.com/cve/CVE-2010-2275/"],
            },
            {
                "below": "1.1",
                "severity": "medium",
                "identifiers": {"CVE": ["CVE-2008-6681"]},
                "info": ["http://www.cvedetails.com/cve/CVE-2008-6681/"],
            },
            {
                "below": "1.10.10",
                "severity": "medium",
                "identifiers": {"PR": "307"},
                "info": [
                    "https://github.com/dojo/dojo/pull/307",
                    "https://dojotoolkit.org/blog/dojo-1-14-released",
                ],
            },
            {
                "atOrAbove": "1.11.0",
                "below": "1.11.6",
                "severity": "medium",
                "identifiers": {"PR": "307"},
                "info": [
                    "https://github.com/dojo/dojo/pull/307",
                    "https://dojotoolkit.org/blog/dojo-1-14-released",
                ],
            },
            {
                "atOrAbove": "1.12.0",
                "below": "1.12.4",
                "severity": "medium",
                "identifiers": {"PR": "307"},
                "info": [
                    "https://github.com/dojo/dojo/pull/307",
                    "https://dojotoolkit.org/blog/dojo-1-14-released",
                ],
            },
            {
                "atOrAbove": "1.13.0",
                "below": "1.13.1",
                "severity": "medium",
                "identifiers": {"PR": "307"},
                "info": [
                    "https://github.com/dojo/dojo/pull/307",
                    "https://dojotoolkit.org/blog/dojo-1-14-released",
                ],
            },
        ],
        "extractors": {
            "func": ["dojo.version.toString()"],
            "uri": [r"/(?:dojo-)?([0-9][0-9.a-z_-]+)/dojo(\.min)?\.js"],
            "filename": [r"dojo-([0-9][0-9.a-z_-]+)(\.min)?\.js"],
            "filecontentreplace": [
                r"/dojo.version={major:([0-9]+),minor:([0-9]+),patch:([0-9]+)/$1.$2.$3/"
            ],
            "hashes": {
                "73cdd262799aab850abbe694cd3bfb709ea23627": "1.4.1",
                "c8c84eddc732c3cbf370764836a7712f3f873326": "1.4.0",
                "d569ce9efb7edaedaec8ca9491aab0c656f7c8f0": "1.0.0",
                "ad44e1770895b7fa84aff5a56a0f99b855a83769": "1.3.2",
                "8fc10142a06966a8709cd9b8732f7b6db88d0c34": "1.3.1",
                "a09b5851a0a3e9d81353745a4663741238ee1b84": "1.3.0",
                "2ab48d45abe2f54cdda6ca32193b5ceb2b1bc25d": "1.2.3",
                "12208a1e649402e362f528f6aae2c614fc697f8f": "1.2.0",
                "72a6a9fbef9fa5a73cd47e49942199147f905206": "1.1.1",
            },
        },
    },
    "angularjs": {
        "bowername": ["angularjs", "angular.js"],
        "vulnerabilities": [
            {
                "atOrAbove": "1.5.0",
                "below": "1.6.9",
                "severity": "low",
                "identifiers": {"summary": "XSS through SVG if enableSvg is set"},
                "info": [
                    "https://github.com/angular/angular.js/blob/master/CHANGELOG.md#169-fiery-basilisk-2018-02-02",
                    "https://vulnerabledoma.in/ngSanitize1.6.8_bypass.html",
                ],
            },
            {
                "atOrAbove": "1.3.0",
                "below": "1.5.0-rc2",
                "severity": "medium",
                "identifiers": {
                    "summary": "The attribute usemap can be used as a security exploit"
                },
                "info": [
                    "https://github.com/angular/angular.js/blob/master/CHANGELOG.md#1230-patronal-resurrection-2016-07-21"
                ],
            },
            {
                "atOrAbove": "1.0.0",
                "below": "1.2.30",
                "severity": "medium",
                "identifiers": {
                    "summary": "The attribute usemap can be used as a security exploit"
                },
                "info": [
                    "https://github.com/angular/angular.js/blob/master/CHANGELOG.md#1230-patronal-resurrection-2016-07-21"
                ],
            },
            {
                "below": "1.6.3",
                "severity": "medium",
                "identifiers": {
                    "summary": "Universal CSP bypass via add-on in Firefox"
                },
                "info": [
                    "https://github.com/mozilla/addons-linter/issues/1000#issuecomment-282083435",
                    "http://pastebin.com/raw/kGrdaypP",
                ],
            },
            {
                "below": "1.6.3",
                "severity": "medium",
                "identifiers": {"summary": "DOS in $sanitize"},
                "info": [
                    "https://github.com/angular/angular.js/blob/master/CHANGELOG.md",
                    "https://github.com/angular/angular.js/pull/15699",
                ],
            },
            {
                "below": "1.6.5",
                "severity": "low",
                "identifiers": {"summary": "XSS in $sanitize in Safari/Firefox"},
                "info": [
                    "https://github.com/angular/angular.js/commit/8f31f1ff43b673a24f84422d5c13d6312b2c4d94"
                ],
            },
        ],
        "extractors": {
            "func": ["angular.version.full"],
            "uri": [r"/([0-9][0-9.a-z_-]+)/angular(\.min)?\.js"],
            "filename": [r"angular(?:js)?-([0-9][0-9.a-z_-]+)(.min)?\.js"],
            "filecontent": [
                r"/\*[ \n]+AngularJS v([0-9][0-9.a-z_-]+)",
                r"http://errors\.angularjs\.org/([0-9][0-9.a-z_-]+)/",
            ],
            "hashes": {},
        },
    },
    "backbone.js": {
        "bowername": ["backbonejs", "backbone"],
        "vulnerabilities": [
            {
                "below": "0.5.0",
                "severity": "medium",
                "identifiers": {
                    "release": "0.5.0",
                    "summary": "cross-site scripting vulnerability",
                },
                "info": ["http://backbonejs.org/#changelog"],
            }
        ],
        "extractors": {
            "func": ["Backbone.VERSION"],
            "uri": [r"/([0-9][0-9.a-z_-]+)/backbone(\.min)?\.js"],
            "filename": [r"backbone(?:js)?-([0-9][0-9.a-z_-]+)(.min)?\.js"],
            "filecontent": [
                r"//[ ]+Backbone.js ([0-9][0-9.a-z_-]+)",
                r'a=t.Backbone={}}a.VERSION="([0-9][0-9.a-z_-]+)"',
            ],
            "hashes": {},
        },
    },
    "mustache.js": {
        "bowername": ["mustache.js", "mustache"],
        "vulnerabilities": [
            {
                "below": "0.3.1",
                "severity": "high",
                "identifiers": {
                    "bug": "112",
                    "summary": "execution of arbitrary javascript",
                },
                "info": ["https://github.com/janl/mustache.js/issues/112"],
            },
            {
                "below": "2.2.1",
                "severity": "medium",
                "identifiers": {
                    "bug": "pull request 530",
                    "summary": "weakness in HTML escaping",
                },
                "info": [
                    "https://github.com/janl/mustache.js/releases/tag/v2.2.1",
                    "https://github.com/janl/mustache.js/pull/530",
                ],
            },
        ],
        "extractors": {
            "func": ["Mustache.version"],
            "uri": [r"/([0-9][0-9.a-z_-]+)/mustache(\.min)?\.js"],
            "filename": [r"mustache(?:js)?-([0-9][0-9.a-z_-]+)(.min)?\.js"],
            "filecontent": [
                r'name:"mustache.js",version:"([0-9][0-9.a-z_-]+)"',
                r"[^a-z]mustache.version[ ]?=[ ]?(?:'|\")([0-9][0-9.a-z_-]+)(?:'|\")",
                r'exports.name[ ]?=[ ]?"mustache.js";[\n ]*exports.version[ ]?=[ ]?(?:\'|")([0-9][0-9.a-z_-]+)(?:\'|");',
            ],
            "hashes": {},
        },
    },
    "handlebars.js": {
        "bowername": ["handlebars", "handlebars.js"],
        "vulnerabilities": [
            {
                "below": "1.0.0.beta.3",
                "severity": "medium",
                "identifiers": {"summary": "poorly sanitized input passed to eval()"},
                "info": ["https://github.com/wycats/handlebars.js/pull/68"],
            },
            {
                "below": "4.0.0",
                "severity": "medium",
                "identifiers": {
                    "summary": "Quoteless attributes in templates can lead to XSS"
                },
                "info": ["https://github.com/wycats/handlebars.js/pull/1083"],
            },
            {
                "atOrAbove": "4.0.0",
                "below": "4.0.13",
                "severity": "high",
                "identifiers": {
                    "summary": "A prototype pollution vulnerability in handlebars is exploitable if an attacker can control the template"
                },
                "info": [
                    "https://snyk.io/vuln/SNYK-JS-HANDLEBARS-173692",
                    "https://github.com/wycats/handlebars.js/commit/7372d4e9dffc9d70c09671aa28b9392a1577fd86",
                ],
            },
            {
                "atOrAbove": "4.0.0",
                "below": "4.0.14",
                "severity": "high",
                "identifiers": {
                    "summary": "A prototype pollution vulnerability in handlebars is exploitable if an attacker can control the template"
                },
                "info": [
                    "https://snyk.io/vuln/SNYK-JS-HANDLEBARS-174183",
                    "https://github.com/wycats/handlebars.js/issues/1495",
                    "https://github.com/wycats/handlebars.js/commit/cd38583216dce3252831916323202749431c773e",
                ],
            },
            {
                "atOrAbove": "4.1.0",
                "below": "4.1.2",
                "severity": "high",
                "identifiers": {
                    "summary": "A prototype pollution vulnerability in handlebars is exploitable if an attacker can control the template"
                },
                "info": [
                    "https://snyk.io/vuln/SNYK-JS-HANDLEBARS-174183",
                    "https://github.com/wycats/handlebars.js/issues/1495",
                    "https://github.com/wycats/handlebars.js/commit/cd38583216dce3252831916323202749431c773e",
                ],
            },
        ],
        "extractors": {
            "func": ["Handlebars.VERSION"],
            "uri": [r"/([0-9][0-9.a-z_-]+)/handlebars(\.min)?\.js"],
            "filename": [r"handlebars(?:js)?-([0-9][0-9.a-z_-]+)(.min)?\.js"],
            "filecontent": [
                r'Handlebars.VERSION = "([0-9][0-9.a-z_-]+)";',
                r"Handlebars=\{VERSION:(?:'|\")([0-9][0-9.a-z_-]+)(?:'|\")",
                r"this.Handlebars=\{\};[\n\r \t]+\(function\([a-z]\)\{[a-z].VERSION=(?:'|\")([0-9][0-9.a-z_-]+)(?:'|\")",
                r"/\*![\n\r \t]+handlebars v([0-9][0-9.a-z_-]+)",
            ],
            "hashes": {},
        },
    },
    "easyXDM": {
        "vulnerabilities": [
            {
                "below": "2.4.18",
                "severity": "high",
                "identifiers": {"CVE": ["CVE-2013-5212"]},
                "info": [
                    "http://blog.kotowicz.net/2013/09/exploiting-easyxdm-part-1-not-usual.html",
                    "http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-5212",
                ],
            },
            {
                "below": "2.4.19",
                "severity": "high",
                "identifiers": {"CVE": ["CVE-2014-1403"]},
                "info": [
                    "http://blog.kotowicz.net/2014/01/xssing-with-shakespeare-name-calling.html",
                    "http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-1403",
                ],
            },
        ],
        "extractors": {
            "uri": [r"/(?:easyXDM-)?([0-9][0-9.a-z_-]+)/easyXDM(\.min)?\.js"],
            "filename": [r"easyXDM-([0-9][0-9.a-z_-]+)(.min)?\.js"],
            "filecontent": [
                r' \* easyXDM\n \* http://easyxdm.net/(?:\r|\n|.)+version:"([0-9][0-9.a-z_-]+)"',
                r"@class easyXDM(?:.|\r|\n)+@version ([0-9][0-9.a-z_-]+)(\r|\n)",
            ],
            "hashes": {"cf266e3bc2da372c4f0d6b2bd87bcbaa24d5a643": "2.4.6"},
        },
    },
    "plupload": {
        "bowername": ["Plupload", "plupload"],
        "vulnerabilities": [
            {
                "below": "1.5.4",
                "severity": "high",
                "identifiers": {"CVE": ["CVE-2012-2401"]},
                "info": ["http://www.cvedetails.com/cve/CVE-2012-2401/"],
            },
            {
                "below": "1.5.5",
                "severity": "high",
                "identifiers": {"CVE": ["CVE-2013-0237"]},
                "info": ["http://www.cvedetails.com/cve/CVE-2013-0237/"],
            },
            {
                "below": "2.1.9",
                "severity": "medium",
                "identifiers": {"CVE": ["CVE-2016-4566"]},
                "info": ["https://github.com/moxiecode/plupload/releases"],
            },
        ],
        "extractors": {
            "func": ["plupload.VERSION"],
            "uri": [r"/([0-9][0-9.a-z_-]+)/plupload(\.min)?\.js"],
            "filename": [r"plupload-([0-9][0-9.a-z_-]+)(.min)?\.js"],
            "filecontent": [
                r"\* Plupload - multi-runtime File Uploader(?:\r|\n)+ \* v([0-9][0-9.a-z_-]+)",
                r'var g=\{VERSION:"([0-9][0-9.a-z_-]+)",.*;window.plupload=g\}',
            ],
            "hashes": {},
        },
    },
    "DOMPurify": {
        "bowername": ["dompurify", "DOMPurify"],
        "vulnerabilities": [
            {
                "below": "0.6.1",
                "severity": "medium",
                "identifiers": {},
                "info": ["https://github.com/cure53/DOMPurify/releases/tag/0.6.1"],
            },
            {
                "below": "0.8.6",
                "severity": "medium",
                "identifiers": {},
                "info": ["https://github.com/cure53/DOMPurify/releases/tag/0.8.6"],
            },
            {
                "below": "0.8.9",
                "severity": "low",
                "identifiers": {"summary": "safari UXSS"},
                "info": [
                    "https://github.com/cure53/DOMPurify/releases/tag/0.8.9",
                    "https://lists.ruhr-uni-bochum.de/pipermail/dompurify-security/2017-May/000006.html",
                ],
            },
            {
                "below": "0.9.0",
                "severity": "low",
                "identifiers": {"summary": "safari UXSS"},
                "info": ["https://github.com/cure53/DOMPurify/releases/tag/0.9.0"],
            },
        ],
        "extractors": {
            "func": ["DOMPurify.version"],
            "filecontent": [
                r"DOMPurify.version = '([0-9][0-9.a-z_-]+)';",
                r'DOMPurify.version="([0-9][0-9.a-z_-]+)"',
                r'DOMPurify=.[^\r\n]{10,500}\.version="([0-9][0-9.a-z_-]+)"',
            ],
            "hashes": {},
        },
    },
    "react": {
        "vulnerabilities": [
            {
                "atOrAbove": "0.4.0",
                "below": "0.4.2",
                "severity": "low",
                "identifiers": {
                    "CVE": ["CVE-2013-7035"],
                    "summary": "potential XSS vulnerability can arise when using user data as a key",
                },
                "info": [
                    "https://facebook.github.io/react/blog/2013/12/18/react-v0.5.2-v0.4.2.html"
                ],
            },
            {
                "atOrAbove": "0.5.0",
                "below": "0.5.2",
                "severity": "low",
                "identifiers": {
                    "CVE": ["CVE-2013-7035"],
                    "summary": "potential XSS vulnerability can arise when using user data as a key",
                },
                "info": [
                    "https://facebook.github.io/react/blog/2013/12/18/react-v0.5.2-v0.4.2.html"
                ],
            },
            {
                "below": "0.14.0",
                "severity": "low",
                "identifiers": {
                    "summary": " including untrusted objects as React children can result in an XSS security vulnerability"
                },
                "info": [
                    "http://danlec.com/blog/xss-via-a-spoofed-react-element",
                    "https://facebook.github.io/react/blog/2015/10/07/react-v0.14.html",
                ],
            },
            {
                "atOrAbove": "16.0.0",
                "below": "16.0.1",
                "severity": "low",
                "identifiers": {
                    "CVE": ["CVE-2018-6341"],
                    "summary": "potential XSS vulnerability when the attacker controls an attribute name",
                },
                "info": [
                    "https://github.com/facebook/react/blob/master/CHANGELOG.md",
                    "https://reactjs.org/blog/2018/08/01/react-v-16-4-2.html",
                ],
            },
            {
                "atOrAbove": "16.1.0",
                "below": "16.1.2",
                "severity": "low",
                "identifiers": {
                    "CVE": ["CVE-2018-6341"],
                    "summary": "potential XSS vulnerability when the attacker controls an attribute name",
                },
                "info": [
                    "https://github.com/facebook/react/blob/master/CHANGELOG.md",
                    "https://reactjs.org/blog/2018/08/01/react-v-16-4-2.html",
                ],
            },
            {
                "atOrAbove": "16.2.0",
                "below": "16.2.1",
                "severity": "low",
                "identifiers": {
                    "CVE": ["CVE-2018-6341"],
                    "summary": "potential XSS vulnerability when the attacker controls an attribute name",
                },
                "info": [
                    "https://github.com/facebook/react/blob/master/CHANGELOG.md",
                    "https://reactjs.org/blog/2018/08/01/react-v-16-4-2.html",
                ],
            },
            {
                "atOrAbove": "16.3.0",
                "below": "16.3.3",
                "severity": "low",
                "identifiers": {
                    "CVE": ["CVE-2018-6341"],
                    "summary": "potential XSS vulnerability when the attacker controls an attribute name",
                },
                "info": [
                    "https://github.com/facebook/react/blob/master/CHANGELOG.md",
                    "https://reactjs.org/blog/2018/08/01/react-v-16-4-2.html",
                ],
            },
            {
                "atOrAbove": "16.4.0",
                "below": "16.4.2",
                "severity": "low",
                "identifiers": {
                    "CVE": ["CVE-2018-6341"],
                    "summary": "potential XSS vulnerability when the attacker controls an attribute name",
                },
                "info": [
                    "https://github.com/facebook/react/blob/master/CHANGELOG.md",
                    "https://reactjs.org/blog/2018/08/01/react-v-16-4-2.html",
                ],
            },
        ],
        "extractors": {
            "func": ["react.version", "require('react').version"],
            "filecontent": [
                r"/\*\*\n +\* React \(with addons\) ?v([0-9][0-9.a-z_-]+)",
                r"/\*\*\n +\* React v([0-9][0-9.a-z_-]+)",
                r'"\./ReactReconciler":[0-9]+,"\./Transaction":[0-9]+,"fbjs/lib/invariant":[0-9]+\}\],[0-9]+:\[function\(require,module,exports\)\{"use strict";module\.exports="([0-9][0-9.a-z_-]+)"\}',
                r'ReactVersion\.js[\*! \\/\n\r]{0,100}function\(e,t\)\{"use strict";e\.exports="([0-9][0-9.a-z_-]+)"',
                r'expected a ReactNode.[\s\S]{0,1800}?function\(e,t\)\{"use strict";e\.exports="([0-9][0-9.a-z_-]+)"',
            ],
        },
    },
    "flowplayer": {
        "vulnerabilities": [
            {
                "below": "5.4.3",
                "severity": "medium",
                "identifiers": {"summary": "XSS vulnerability in Flash fallback"},
                "info": ["https://github.com/flowplayer/flowplayer/issues/381"],
            }
        ],
        "extractors": {
            "uri": [r"flowplayer-([0-9][0-9.a-z_-]+)(\.min)?\.js"],
            "filename": [r"flowplayer-([0-9][0-9.a-z_-]+)(\.min)?\.js"],
        },
    },
    "DWR": {
        "vulnerabilities": [
            {
                "below": "1.1.4",
                "severity": "high",
                "identifiers": {"CVE": ["CVE-2007-01-09"]},
                "info": [
                    "http://www.cvedetails.com/cve/CVE-2014-5326/",
                    "http://www.cvedetails.com/cve/CVE-2014-5326/",
                ],
            },
            {
                "below": "2.0.11",
                "severity": "medium",
                "identifiers": {"CVE": ["CVE-2014-5326", "CVE-2014-5325"]},
                "info": [
                    "http://www.cvedetails.com/cve/CVE-2014-5326/",
                    "http://www.cvedetails.com/cve/CVE-2014-5326/",
                ],
            },
            {
                "above": "3",
                "below": "3.0.RC3",
                "severity": "medium",
                "identifiers": {"CVE": ["CVE-2014-5326", "CVE-2014-5325"]},
                "info": [
                    "http://www.cvedetails.com/cve/CVE-2014-5326/",
                    "http://www.cvedetails.com/cve/CVE-2014-5326/",
                ],
            },
        ],
        "extractors": {
            "func": ["dwr.version"],
            "filecontent": [r" dwr-([0-9][0-9.a-z_-]+).jar"],
        },
    },
    "moment.js": {
        "bowername": ["moment", "momentjs"],
        "vulnerabilities": [
            {
                "below": "2.11.2",
                "severity": "low",
                "identifiers": {
                    "summary": "reDOS - regular expression denial of service"
                },
                "info": ["https://github.com/moment/moment/issues/2936"],
            }
        ],
        "extractors": {
            "func": ["moment.version"],
            "filecontent": [
                r"//! moment.js(?:[\n\r]+)//! version : ([0-9][0-9.a-z_-]+)"
            ],
        },
    },
    "bootstrap": {
        "vulnerabilities": [
            {
                "below": "4.3.1",
                "atOrAbove": "4.0.0",
                "identifiers": {
                    "issue": "28236",
                    "summary": "XSS in data-template, data-content and data-title properties of tooltip/popover",
                    "CVE": ["CVE-2019-8331"],
                },
                "severity": "high",
                "info": ["https://github.com/twbs/bootstrap/issues/28236"],
            },
            {
                "below": "3.4.1",
                "identifiers": {
                    "issue": "28236",
                    "summary": "XSS in data-template, data-content and data-title properties of tooltip/popover",
                    "CVE": ["CVE-2019-8331"],
                },
                "severity": "high",
                "info": ["https://github.com/twbs/bootstrap/issues/28236"],
            },
            {
                "below": "4.1.2",
                "atOrAbove": "4.0.0",
                "identifiers": {
                    "issue": "20184",
                    "summary": "XSS in data-target property of scrollspy",
                    "CVE": ["CVE-2018-14041"],
                },
                "severity": "medium",
                "info": ["https://github.com/twbs/bootstrap/issues/20184"],
            },
            {
                "below": "3.4.0",
                "identifiers": {
                    "issue": "20184",
                    "summary": "XSS in data-target property of scrollspy",
                    "CVE": ["CVE-2018-14041"],
                },
                "severity": "medium",
                "info": ["https://github.com/twbs/bootstrap/issues/20184"],
            },
            {
                "below": "4.1.2",
                "atOrAbove": "4.0.0",
                "identifiers": {
                    "issue": "20184",
                    "summary": "XSS in collapse data-parent attribute",
                    "CVE": ["CVE-2018-14040"],
                },
                "severity": "medium",
                "info": ["https://github.com/twbs/bootstrap/issues/20184"],
            },
            {
                "below": "3.4.0",
                "identifiers": {
                    "issue": "20184",
                    "summary": "XSS in collapse data-parent attribute",
                    "CVE": ["CVE-2018-14040"],
                },
                "severity": "medium",
                "info": ["https://github.com/twbs/bootstrap/issues/20184"],
            },
            {
                "below": "4.1.2",
                "atOrAbove": "4.0.0",
                "identifiers": {
                    "issue": "20184",
                    "summary": "XSS in data-container property of tooltip",
                    "CVE": ["CVE-2018-14042"],
                },
                "severity": "medium",
                "info": ["https://github.com/twbs/bootstrap/issues/20184"],
            },
            {
                "below": "3.4.0",
                "identifiers": {
                    "issue": "20184",
                    "summary": "XSS in data-container property of tooltip",
                    "CVE": ["CVE-2018-14042"],
                },
                "severity": "medium",
                "info": ["https://github.com/twbs/bootstrap/issues/20184"],
            },
            {
                "below": "2.1.0",
                "severity": "medium",
                "identifiers": {"summary": "cross-site scripting vulnerability"},
                "info": ["https://github.com/twbs/bootstrap/pull/3421"],
            },
        ],
        "extractors": {
            "uri": [r"/([0-9][0-9.a-z_-]+)/bootstrap(\.min)?\.js"],
            "filename": [r"bootstrap-([0-9][0-9.a-z_-]+)(\.min)?\.js"],
            "filecontent": [
                r"/\*!? Bootstrap v([0-9][0-9.a-z_-]+)",
                r"\* Bootstrap v([0-9][0-9.a-z_-]+)",
                r"/\*! Bootstrap v([0-9][0-9.a-z_-]+)",
            ],
            "hashes": {},
        },
    },
    "ckeditor": {
        "vulnerabilities": [
            {
                "below": "4.4.3",
                "identifiers": {"summary": "XSS"},
                "severity": "medium",
                "info": [
                    "https://github.com/ckeditor/ckeditor-dev/blob/master/CHANGES.md#ckeditor-443"
                ],
            },
            {
                "below": "4.4.6",
                "identifiers": {"summary": "XSS"},
                "severity": "medium",
                "info": [
                    "https://github.com/ckeditor/ckeditor-dev/blob/master/CHANGES.md#ckeditor-446"
                ],
            },
            {
                "below": "4.4.8",
                "identifiers": {"summary": "XSS"},
                "severity": "medium",
                "info": [
                    "https://github.com/ckeditor/ckeditor-dev/blob/master/CHANGES.md#ckeditor-448"
                ],
            },
            {
                "below": "4.5.11",
                "identifiers": {"summary": "XSS"},
                "severity": "medium",
                "info": [
                    "https://github.com/ckeditor/ckeditor-dev/blob/master/CHANGES.md#ckeditor-4511"
                ],
            },
            {
                "below": "4.9.2",
                "atOrAbove": "4.5.11",
                "identifiers": {
                    "summary": "XSS if the enhanced image plugin is installed"
                },
                "severity": "medium",
                "info": [
                    "https://ckeditor.com/blog/CKEditor-4.9.2-with-a-security-patch-released/",
                    "https://ckeditor.com/cke4/release-notes",
                ],
            },
            {
                "atOrAbove": "4.0.0",
                "below": "4.11.0",
                "identifiers": {"summary": "XSS vulnerability in the HTML parser"},
                "severity": "medium",
                "info": [
                    "https://ckeditor.com/blog/CKEditor-4.11-with-emoji-dropdown-and-auto-link-on-typing-released/",
                    "https://snyk.io/vuln/SNYK-JS-CKEDITOR-72618",
                ],
            },
        ],
        "extractors": {
            "uri": [r"/([0-9][0-9.a-z_-]+)/ckeditor(\.min)?\.js"],
            "filename": [r"ckeditor-([0-9][0-9.a-z_-]+)(\.min)?\.js"],
            "filecontent": [
                r'ckeditor..js.{4,20}=\{timestamp:"[^"]+",version:"([0-9][0-9.a-z_-]+)',
                r'window.CKEDITOR=function\(\)\{var [a-z]=\{timestamp:"[^"]+",version:"([0-9][0-9.a-z_-]+)',
            ],
            "hashes": {},
            "func": ["CKEDITOR.version"],
        },
    },
    "vue": {
        "vulnerabilities": [
            {
                "below": "2.5.17",
                "severity": "medium",
                "identifiers": {"summary": "potential xss in ssr when using v-bind"},
                "info": ["https://github.com/vuejs/vue/releases/tag/v2.5.17"],
            },
            {
                "below": "2.4.3",
                "severity": "medium",
                "identifiers": {"summary": "possible xss vector "},
                "info": ["https://github.com/vuejs/vue/releases/tag/v2.4.3"],
            },
        ],
        "extractors": {
            "uri": [r"/vue@([0-9][0-9.a-z_-]+)/dist/vue\.js"],
            "filename": [r"vue-([0-9][0-9.a-z_-]+)(\.min)?\.js"],
            "filecontent": [
                r"/\*!\n * Vue.js v([0-9][0-9.a-z_-]+)",
                r"Vue.version = '([0-9][0-9.a-z_-]+)';",
                r"'([0-9][0-9.a-z_-]+)'[^\n]{0,8000}Vue compiler",
            ],
            "func": ["Vue.version"],
        },
    },
    "ExtJS": {
        "vulnerabilities": [
            {
                "below": "6.6.0",
                "atOrAbove": "4.0.0",
                "severity": "high",
                "identifiers": {
                    "CVE": ["CVE-2018-8046"],
                    "summary": "XSS in Sencha Ext JS 4 to 6 via getTip() method of Action Columns",
                },
                "info": [
                    "http://seclists.org/fulldisclosure/2018/Jul/8",
                    "https://nvd.nist.gov/vuln/detail/CVE-2018-8046",
                ],
            },
            {
                "below": "6.0.0",
                "severity": "high",
                "identifiers": {
                    "CVE": ["CVE-2007-2285"],
                    "summary": "Directory traversal and arbitrary file read",
                },
                "info": [
                    "https://www.cvedetails.com/cve/CVE-2007-2285/",
                    "https://packetstormsecurity.com/files/132052/extjs-Arbitrary-File-Read.html",
                    "https://www.akawebdesign.com/2018/08/14/should-js-frameworks-prevent-xss/",
                ],
            },
            {
                "below": "4.0.0",
                "atOrAbove": "3.0.0",
                "severity": "high",
                "identifiers": {
                    "CVE": ["CVE-2010-4207", "CVE-2012-5881"],
                    "summary": "XSS vulnerability in ExtJS charts.swf",
                },
                "info": [
                    "https://www.acunetix.com/vulnerabilities/web/extjs-charts-swf-cross-site-scripting",
                    "https://typo3.org/security/advisory/typo3-core-sa-2014-001/",
                    "https://www.akawebdesign.com/2018/08/14/should-js-frameworks-prevent-xss/",
                ],
            },
        ],
        "extractors": {
            "uri": [r"/extjs/([0-9][0-9.a-z_-]+)/.*\.js"],
            "filename": [
                r"/ext-all-([0-9][0-9.a-z_-]+)(\.min)?.js",
                r"/ext-all-debug-([0-9][0-9.a-z_-]+)(\.min)?.js",
                r"/ext-base-([0-9][0-9.a-z_-]+)(\.min)?.js",
            ],
            "filecontent": [r"/*!\n * Ext JS Library ([0-9][0-9.a-z_-]+)"],
            "func": [
                "Ext && Ext.versions && Ext.versions.extjs.version",
                "Ext && Ext.version",
            ],
        },
    },
    "dont check": {
        "extractors": {
            "uri": [
                "^http[s]?://(ssl|www).google-analytics.com/ga.js",
                "^http[s]?://apis.google.com/js/plusone.js",
                "^http[s]?://cdn.cxense.com/cx.js",
            ]
        }
    },
}
