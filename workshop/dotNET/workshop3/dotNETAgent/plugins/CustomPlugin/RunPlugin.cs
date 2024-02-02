using System.ComponentModel;
using System.Globalization;
using System.Threading.Tasks;
using System.Diagnostics;

using Microsoft.SemanticKernel;


    public class RunPlugin
    {
        [KernelFunction,Description("running code")]
        public string RunDotNETCLI(string cli)
        {

            Console.WriteLine("--------------------------------------------------------");
            Console.WriteLine("----------------Running dotNET CLI---------------------");
            Console.WriteLine(cli);
            Console.WriteLine("--------------------------------------------------------");

            using(Process process = new Process())
            {
                process.StartInfo.FileName = "dotnet";
                process.StartInfo.Arguments = cli.Replace("dotnet","").Replace("```bash","").Replace("```","").ToString();//"run --project ./workspace/helloworld";
                process.StartInfo.UseShellExecute = false;
                process.StartInfo.RedirectStandardOutput = true;
                process.StartInfo.RedirectStandardError = true;
                process.Start();

                string output = process.StandardOutput.ReadToEnd();

                return output;
            }
        }

    }