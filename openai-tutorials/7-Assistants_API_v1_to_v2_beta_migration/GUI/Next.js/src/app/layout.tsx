import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./styles/global.scss";
import { AppRouterCacheProvider } from "@mui/material-nextjs/v14-appRouter";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Next.js GUI for the OpenAI Assistants API v2 beta",
  description: "Next.js GUI for the OpenAI Assistants API v2 beta",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <AppRouterCacheProvider>{children}</AppRouterCacheProvider>
      </body>
    </html>
  );
}
