"use client";

import {
  Menu,
  LayoutDashboard,
  Upload,
  MessageSquare,
  ShieldAlert,
  FileSearch,
  BarChart3,
  Download,
  Settings,
} from "lucide-react";

import {
  Sheet,
  SheetContent,
  SheetTrigger,
} from "@/components/ui/sheet";

import { Button } from "@/components/ui/button";

const menuItems = [
  { icon: LayoutDashboard, title: "Dashboard" },
  { icon: Upload, title: "Upload Contract" },
  { icon: MessageSquare, title: "AI Chat" },
  { icon: ShieldAlert, title: "Risk Dashboard" },
  { icon: FileSearch, title: "Clause Explorer" },
  { icon: BarChart3, title: "Analytics" },
  { icon: Download, title: "Reports" },
  { icon: Settings, title: "Settings" },
];

export default function MobileSidebar() {
  return (
    <Sheet>
      <SheetTrigger className="md:hidden">
        <Menu size={20} />
        </SheetTrigger>

      <SheetContent side="left" className="w-72">
        <div className="mb-8">
          <h2 className="text-xl font-bold">
            Contract AI
          </h2>

          <p className="text-sm text-muted-foreground">
            Risk Analysis Platform
          </p>
        </div>

        <nav className="space-y-2">
          {menuItems.map(({ icon: Icon, title }) => (
            <Button
              key={title}
              variant="ghost"
              className="w-full justify-start gap-3"
            >
              <Icon size={18} />
              {title}
            </Button>
          ))}
        </nav>
      </SheetContent>
    </Sheet>
  );
}