# from semantic_kernel.skill_definition import sk_function, sk_function_context_parameter
from semantic_kernel.functions import kernel_function


class CustomPlugin:
    @kernel_function(
        description = "Get news from the web",
        name = "NewsPlugin"
    )
    def get_news_api(self, location: str) -> str:
        return """Get news from the """ + location + """."""
    
    @kernel_function(
            description="Search Weather in a city",
            name="WeatherFunction"
        )
    def ask_weather_function(self, city: str) -> str:
        return city + "’s weather is 30 celsius degree , and very hot."
    
    @kernel_function(
            description="Search Docs",
            name="DocsFunction" 
        )
    def ask_docs_function(self, doc: str) -> str:
        return "ask docs :" + doc