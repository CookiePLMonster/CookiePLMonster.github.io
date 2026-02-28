# Extends {% link %} with pass-through for absolute URLs
module Jekyll
  module Tags
    class Link
      alias_method :original_render, :render

      def render(context)
        relative_path = Liquid::Template.parse(@relative_path).render(context)
        if relative_path.include?('://')
          relative_path.strip
        else
          original_render(context)
        end
      end
    end
  end
end
