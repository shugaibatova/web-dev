def close_far(a, b, c):
  def close(x, y): return abs(x - y) <= 1
  def far(x, y): return abs(x - y) >= 2
  return (close(b, a) and far(c, a) and far(c, b) or
            close(c, a) and far(b, a) and far(b, c))