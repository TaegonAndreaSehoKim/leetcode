class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        counter = {}
        result= []
        for cpdomain in cpdomains:
            count_str, domain = cpdomain.split()
            count = int(count_str)
            parts = domain.split(".")
            for i in range(len(parts)):
                subdomain = ".".join(parts[i:])
                counter[subdomain] = counter.get(subdomain, 0) + count
        for subdomain, counter_num in counter.items():
            result.append(str(counter_num) + " " + subdomain)
        return result