class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        """
        :type code: List[str]
        :type businessLine: List[str]
        :type isActive: List[bool]
        :rtype: List[str]
        """

        valid_lines = ["electronics", "grocery", "pharmacy", "restaurant"]
        order = {line: i for i, line in enumerate(valid_lines)}

        valid = []

        for c, b, active in zip(code, businessLine, isActive):
            if not active:
                continue

            if b not in order:
                continue

            if not c or not c.replace("_", "").isalnum():
                continue

            valid.append((order[b], c))

        valid.sort()

        return [c for _, c in valid]
