using Microsoft.SemanticKernel;
using System.ComponentModel;
using System.Globalization;


public class CompanySearchPlugin
{
    [KernelFunction,Description("search employee infomation")]
    public string EmployeeSearch(string input)
    {
        return "欢迎了解社保相关内容";
    }

    [KernelFunction,Description("search weather")]
    public string WeatherSearch(string city)
    {
        return city + ", 2 degree,rainy";
    }
}