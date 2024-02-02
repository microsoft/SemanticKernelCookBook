using System.ComponentModel;
using System.Globalization;
using System.Threading.Tasks;

using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.Connectors.OpenAI;


    public class GenCLIPlugin
    {
        [KernelFunction,Description("cli generation")]
        public async Task<string> GenDotNETCLI(string request)
        {
            Kernel kernel = Kernel.CreateBuilder()
                        .AddAzureOpenAIChatCompletion("gpt-4-32k", Settings.AOAIEndpoint, Settings.AOAIKey)
                        .Build();

            var pluginDirectory = Path.Combine("./", "plugins");

            var code_plugin = kernel.CreatePluginFromPromptDirectory(Path.Combine(pluginDirectory, "CodePlugin"));


            // Console.WriteLine("0000");
            // Console.WriteLine(cmd);
            // Console.WriteLine("0000");

            var code = await kernel.InvokeAsync(code_plugin["dotNET"],new(){["request"] = request});

            // // var gen_code = code.Replace("```bash","").Replace("```","").ToString();
            Console.WriteLine("--------------------------------------------------------");
            Console.WriteLine("---------------------Gen dotNET CLI---------------------");
            Console.WriteLine(code);
            Console.WriteLine("--------------------------------------------------------");

            return code.ToString();
        }
    }