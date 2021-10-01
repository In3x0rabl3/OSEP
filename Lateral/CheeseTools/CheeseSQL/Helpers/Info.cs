namespace CheeseSQL.Helpers
{
    public static class Info
    {
        public static void ShowLogo()
        {
        }

        public static void ShowUsage()
        {
            var collection = new CommandCollection();
            collection.ShowUsage();
        }

    }
}