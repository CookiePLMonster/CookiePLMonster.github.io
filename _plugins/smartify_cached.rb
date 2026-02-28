# Source: https://alexwlchan.net/2024/jekyll-caching/
module Jekyll
  module Filters
    alias builtin_smartify smartify

    def smartify_cache
      @@smartify_cache ||= Jekyll::Cache.new('Smartify')
    end

    # Like the builtin smartify filter, but faster.
    def smartify(input)
      smartify_cache.getset(input) do
        builtin_smartify(input)
      end
    end
  end
end
