def make_bricks(small, big, goal):
  return goal % 5 <= small and goal - min(goal // 5, big) * 5 <= small
