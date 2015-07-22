import re
import unittest

from dice.utils import rnd


class RndRegexTest(unittest.TestCase):
    def test_rnd_regex(self):
        patts = [
            r"[a-fA-F0-9]{32}",
            r"[a-fA-F0-9]{8}\-([a-fA-F0-9]{4}\-){3}[a-fA-F0-9]{12}",
            r"[0-9]+",
            r"[a-zA-Z0-9\-_\.]+",
            r"[a-zA-Z0-9/\-_\. \(\)]+",
            r"""/[a-zA-Z0-9_\.\+\-\\&"'<>/%,]+""",
            r"-?[0-9]+",
            r"[a-zA-Z0-9_\.\-]+",
            r"[0-9]{1,2}",
            r"[a-zA-Z0-9_\.\+\-/]+",
            r"[a-zA-Z0-9_\-.]+",
            r"(0x)?[0-9a-fA-F]{1,4}",
            r"(0x)?[0-9a-fA-F]{1,2}",
            r"(0x)?[0-9a-fA-F]{1,16}",
            r"(0x)?[0-9a-fA-F]{1,3}",
            r"0x[a-fA-F0-9]{1,4}",
            r"[a-zA-Z0-9_\.\-\\:/]+",
            r"((0x)?[0-9a-fA-F]{1,3}\.){0,3}(0x)?[0-9a-fA-F]{1,3}",
            r"0x[fF][0-9a-eA-E]?",
            r"0x[a-fA-F0-9]",
            r"[a-zA-Z0-9_]+",
            r"[a-fA-F0-9][02468aAcCeE](:[a-fA-F0-9]{2}){5}",
            r"(0x)?[0-1]?[0-9a-fA-F]",
            r"[a-zA-Z0-9_\+\-]+",
            r"0x[0-9a-eA-E][0-9a-fA-F]?",
            r"(0x)?[0-7]",
            r"-1",
            r"""[a-zA-Z0-9_\.\+\-\\&"'<>/%]+""",
            r"[a-zA-Z0-9\-_]+",
            r"[a-zA-Z0-9_\.:]+",
            r"(0x)?[0-3]",
            r"0x[0-9a-fA-F]{1,4}",
            r"""/[a-zA-Z0-9_\.\+\-\\&"'<>/%]*""",
            r"[a-zA-Z0-9\.\-]+",
            r"[0-9]{1,2}.[0-9]{1,2}",
            r"0x[0-9a-fA-F]{1,2}",
            r"0x[0-9a-fA-F]{1,6}",
            r"(0x)?[0-9a-fA-F]{16}",
            r"(-|\+)?[0-9]+",
            r"(ab|cde|fga)",
            r"(a|b)",
            r"(a)|(b(c))",
            r"a|b",
            r"(([0-2]?[0-9]?[0-9]\.){3}[0-2]?[0-9]?[0-9])|(([0-9a-fA-F]+|:)+"
            "[0-9a-fA-F]+)|([a-zA-Z0-9_\.\+\-]*)",
            r"(((25[0-5])|(2[0-4][0-9])|(1[0-9]{2})|([1-9][0-9])|([0-9]))\.)"
            "{3}((25[0-5])|(2[0-4][0-9])|(1[0-9]{2})|([1-9][0-9])|([0-9]))",
            r"([0-9]+(-[0-9]+)?|\^[0-9]+)(,([0-9]+(-[0-9]+)?|\^[0-9]+))*",
            r"a(b|c)",
            r"[^\n]+",
            r"[^,a]{12}",
            r"[^/]+",
            r"(vepa|bridge|private|passthrough)",
            r"(ioemu:)?(fd|hd|sd|vd|xvd|ubd)[a-zA-Z0-9_]+",
            r"[A-Za-z0-9_\.\+\-]+",
            r"[x20-x7E]{0,8}",
            r"(([0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4})|(([0-9A-Fa-f]{1,4}:){6}"
            ":[0-9A-Fa-f]{1,4})|(([0-9A-Fa-f]{1,4}:){5}:([0-9A-Fa-f]{1,4}:)?"
            "[0-9A-Fa-f]{1,4})|(([0-9A-Fa-f]{1,4}:){4}:([0-9A-Fa-f]{1,4}:)"
            "{0,2}[0-9A-Fa-f]{1,4})|(([0-9A-Fa-f]{1,4}:){3}:([0-9A-Fa-f]{1,4}"
            ":){0,3}[0-9A-Fa-f]{1,4})|(([0-9A-Fa-f]{1,4}:){2}:([0-9A-Fa-f]"
            "{1,4}:){0,4}[0-9A-Fa-f]{1,4})|(([0-9A-Fa-f]{1,4}:){6}(((25[0-5])"
            "|(2[0-4][0-9])|(1[0-9]{2})|([1-9][0-9])|([0-9]))\.){3}((25[0-5])"
            "|(2[0-4][0-9])|(1[0-9]{2})|([1-9][0-9])|([0-9])))|(([0-9A-Fa-f]"
            "{1,4}:){0,5}:(((25[0-5])|(2[0-4][0-9])|(1[0-9]{2})|([1-9][0-9])"
            "|([0-9]))\.){3}((25[0-5])|(2[0-4][0-9])|(1[0-9]{2})|([1-9][0-9])"
            "|([0-9])))|(::([0-9A-Fa-f]{1,4}:){0,5}(((25[0-5])|(2[0-4][0-9])"
            "|(1[0-9]{2})|([1-9][0-9])|([0-9]))\.){3}((25[0-5])|(2[0-4][0-9])"
            "|(1[0-9]{2})|([1-9][0-9])|([0-9])))|([0-9A-Fa-f]{1,4}::"
            "([0-9A-Fa-f]{1,4}:){0,5}[0-9A-Fa-f]{1,4})|(::([0-9A-Fa-f]{1,4}:)"
            "{0,6}[0-9A-Fa-f]{1,4})|(([0-9A-Fa-f]{1,4}:){1,7}:)",
            # r"-[^-]",
        ]
        for patt in patts:
            for i in range(100):
                res = rnd.regex(patt)
                m = re.match(patt + '$', res)
                self.assertIsNotNone(m)

if __name__ == '__main__':
    unittest.main()
