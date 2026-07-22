"use client";

import { Bell, Search } from "lucide-react";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import ThemeToggle from "@/components/ui/theme-toggle";
import MobileSidebar from "./mobile-sidebar";

export default function Navbar() {
  return (
    <header className="sticky top-0 z-50 flex h-16 items-center justify-between border-b bg-background/95 px-6 backdrop-blur">
      <div className="flex items-center gap-4">
        <MobileSidebar />

        <div>
          <h2 className="text-2xl font-bold tracking-tight">
            Dashboard
          </h2>

          <p className="text-sm text-muted-foreground">
            AI Contract Risk Analysis Platform
          </p>
        </div>
      </div>

      <div className="flex items-center gap-4">
        <div className="relative hidden lg:block">
          <Search
            className="absolute left-3 top-1/2 -translate-y-1/2 text-muted-foreground"
            size={18}
          />

          <Input
            className="w-80 pl-10"
            placeholder="Search contracts..."
          />
        </div>

        <div className="flex items-center gap-2">
          <ThemeToggle />

          <Button variant="outline" size="icon">
            <Bell size={18} />
          </Button>
        </div>

        <div className="flex items-center gap-3 rounded-xl border px-3 py-2">
          <div className="flex h-10 w-10 items-center justify-center rounded-full bg-blue-600 text-white font-semibold">
            R
          </div>

          <div className="hidden md:block">
            <p className="text-sm font-semibold">
              Ragini
            </p>

            <p className="text-xs text-muted-foreground">
              AI Engineer
            </p>
          </div>
        </div>
      </div>
    </header>
  );
}