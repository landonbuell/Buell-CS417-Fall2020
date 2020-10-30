using System;
using System.IO;
using System.IO.Compression;

namespace ZipFileTest
{
    class ZipFileMain
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            string zipPath = @"C:\Users\Landon\Documents\GitHub\Buell-CS417-Fall2020\Lab14\Lab14\archive.zip";
            string extPath = @"C:\Users\Landon\Documents\GitHub\Buell-CS417-Fall2020\Lab14";

            using (FileStream zipToOpen = new FileStream(zipPath, FileMode.Open))
            {
                using (ZipArchive archive = new ZipArchive(zipToOpen, ZipArchiveMode.Update))
                {
                    ZipArchiveEntry readmeEntry = archive.CreateEntry("Readme.txt");
                    using (StreamWriter writer = new StreamWriter(readmeEntry.Open()))
                    {
                        writer.WriteLine("Information about this package.");
                        writer.WriteLine("========================");
                    }
                }
            }


        }
    }
}
