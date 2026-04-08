class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            # If a is positive, it moves right; it can't collide yet.
            if a > 0:
                stack.append(a)
                continue

            # a < 0: asteroid moves left; it may collide with positives on the stack
            while stack and stack[-1] > 0:
                if stack[-1] < -a:
                    # top dies, continue checking with new top
                    stack.pop()
                    continue
                elif stack[-1] == -a:
                    # both die
                    stack.pop()
                    break
                else:
                    # current a dies
                    break
            else:
                # No positive asteroid to collide with, current a survives
                if not stack or stack[-1] <= 0:
                    stack.append(a)

        return stack