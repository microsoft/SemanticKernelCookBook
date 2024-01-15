from semantic_kernel.skill_definition import sk_function, sk_function_context_parameter
from semantic_kernel import SKContext


class API:
    @sk_function(
        description = "Get news from the web",
        name = "NewsPlugin"
    )
    @sk_function_context_parameter(name="location", description="location name")
    def get_news_api(self, context: SKContext) -> str:
        return """Get news from the """ + context["location"] + """."""
    
    @sk_function(
            description="Search Weather in a city",
            name="WeatherFunction"
        )
    @sk_function_context_parameter(name="city", description="city string")
    def ask_weather_function(self, context: SKContext) -> str:
        return "Guangzhou’s weather is 30 celsius degree , and very hot."
    
    @sk_function(
            description="Search Docs",
            name="DocsFunction" 
        )
    @sk_function_context_parameter(name="docs", description="docs string")
    def ask_docs_function(self, context: SKContext) -> str:
        return "ask docs :" + context["docs"]