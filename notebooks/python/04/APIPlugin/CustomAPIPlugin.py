from semantic_kernel.functions import kernel_function


class CustomAPIPlugin:
    @kernel_function(
        name = "NewsPlugin",
        description = "Get news from the web",
    )
    def get_news_api(self,location:str) -> str:
        return """Get news from the """ + location + """."""
    
    @kernel_function(
            name="WeatherFunction",
            description="Search Weather in a city",
        )
    def ask_weather_function(self,city: str) -> str:
        return city + "’s weather is 30 celsius degree , and very hot."
    
    @kernel_function(
            name="DocsFunction",
            description="Search Docs",
        )
    def ask_docs_function(self,docs: str) -> str:
        return "ask docs :" + docs