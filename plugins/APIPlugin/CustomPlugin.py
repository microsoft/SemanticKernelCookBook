# from semantic_kernel.skill_definition import sk_function, sk_function_context_parameter
from semantic_kernel import SKContext
from semantic_kernel.plugin_definition import kernel_function,kernel_function_context_parameter


class CustomPlugin:
    @kernel_function(
        description = "Get news from the web",
        name = "NewsPlugin"
    )
    @kernel_function_context_parameter(name="location", description="location name")
    def get_news_api(self, context: SKContext) -> str:
        return """Get news from the """ + context["location"] + """."""
    
    @kernel_function(
            description="Search Weather in a city",
            name="WeatherFunction"
        )
    @kernel_function_context_parameter(name="city", description="city string")
    def ask_weather_function(self, context: SKContext) -> str:
        return "Guangzhou’s weather is 30 celsius degree , and very hot."
    
    @kernel_function(
            description="Search Docs",
            name="DocsFunction" 
        )
    @kernel_function_context_parameter(name="docs", description="docs string")
    def ask_docs_function(self, context: SKContext) -> str:
        return "ask docs :" + context["docs"]