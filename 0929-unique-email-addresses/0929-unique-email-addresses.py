class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        email_set = set()
        for email in emails:
            local, domain = email.split("@")
            processed_local = ""
            for char in local:
                if char == ".":
                    continue
                elif char == "+":
                    break
                else:
                    processed_local += char
            email_set.add(processed_local + "@" + domain)
        return len(email_set)