from textual import events
from textual.app import App
from textual.widgets import Placeholder


class SimpleApp(App):

    async def on_mount(self, event: events.Mount) -> None:
        await self.view.dock(Placeholder(), edge="left", size=40)
        await self.view.dock(Placeholder(), Placeholder(), edge="top")

    async def on_load(self, event):
        await self.bind("up", "color('red')")

    async def action_color(self, color:str) -> None:
        a,b = self.get_widget_at(0,0)
        await self.set_focus(a)

SimpleApp.run(log="textual.log")
