class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_counter = {}

        for cp in cpdomains:
            count, domain = cp.split(' ')
            count = int(count)

            if domain not in domain_counter:
                domain_counter[domain] = 0
            domain_counter[domain] += count


            parts = domain.split('.')

            for i in range(1, len(parts)):
                parent = '.'.join(parts[i:])

                if parent not in domain_counter:
                    domain_counter[parent] = 0
                domain_counter[parent] += count

        res = []

        for domain, count in domain_counter.items():
            res.append(f'{count} {domain}')

        return res
        