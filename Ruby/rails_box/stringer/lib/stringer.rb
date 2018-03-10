require "stringer/version"

module Stringer
  # Your code goes here...
  def self.spacify(*strings)
    string = ""
    strings.each do |s|
      string += s + " "
    end
    return string.rstrip
  end

  def self.minify(string, len)
    if string.length <= len
      return string.rstrip
    else
      return string[0...len].rstrip + "..."
    end
  end

  def self.replacify(string, look, repl)
    return string.gsub! look, repl
  end

  def self.tokenize(string)
    arr = []
    string.split(' ').each do |s|
      arr.push(s)
    end
    return arr
  end

  def self.removify(string, rem)
    return string.sub!(rem,'').squeeze(' ')
  end
end
