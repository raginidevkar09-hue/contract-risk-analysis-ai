"use client";

import {
  LayoutDashboard,
  Upload,
 MessageSquare,
  ShieldAlert,
  FileSearch,
  BarChart3,
  Download,
  Settings,
} from "lucide-react";

const menuItems = [
  { icon: LayoutDashboard, title: "Dashboard", active: true },
  { icon: Upload, title: "Upload Contract" },
  { icon: MessageSquare, title: "AI Chat" },
  { icon: ShieldAlert, title: "Risk Dashboard" },
  { icon: FileSearch, title: "Clause Explorer" },
  { icon: BarChart3, title: "Analytics" },
  { icon: Download, title: "Reports" },
  { icon: Settings, title: "Settings" },
];

export default function Sidebar() {
  return (
    <aside className="sticky top-0 flex h-screen w-72 flex-col border-r bg-background">
      {/* Logo */}
      <div className="border-b px-6 py-5">
        <h1 className="text-2xl font-bold tracking-tight">
          Contract AI
        </h1>

        <p className="mt-1 text-sm text-muted-foreground">
          Risk Analysis Platform
        </p>
      </div>

      {/* Navigation */}
      <nav className="flex-1 space-y-2 overflow-y-auto p-4">
        {menuItems.map(({ icon: Icon, title, active }) => (
          <button
            key={title}
            className={`flex w-full items-center gap-3 rounded-xl px-4 py-3 text-left transition-all duration-200 ${
              active
                ? "bg-blue-600 text-white shadow-md"
                : "text-foreground hover:bg-muted"
            }`}
          >
            <Icon size={20} />
            <span className="font-medium">{title}</span>
          </button>
        ))}
      </nav>

      {/* Footer */}
      <div className="border-t p-5">
        <div className="rounded-xl border bg-muted p-4">
          <p className="font-semibold">
            AI Contract Risk Analysis
          </p>

          <p className="mt-1 text-sm text-muted-foreground">
            Portfolio SaaS Project
          </p>
        </div>
      </div>
    </aside>
  );
}