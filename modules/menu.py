
import module

class Module(module.Module):

    menu_pages = None

    def __init__(self, base_path):
        pass

    def interpret_config(self, page, site, source_path, source, file_name, default, configPage, children, parents, index, bodyhtml):
        self.menu_pages = []
        for menu in site['menu']:
            self.menu_pages.append({})

        if 'menuTitle' not in page:
            page['menuTitle'] = page['title']

        for index, menu in enumerate(site['menu']):
            if configPage in menu:
                self.menu_pages[index][configPage] = page

    def render(self, site, dist, base):
        file = open(base+'/html/menu.html', 'r')
        menu_html = file.read()
        file.close()

        for index, menu in enumerate(site['menu']):
            site['menu[%d]' % index] = ''
            for path in menu:
                if path in self.menu_pages[index]:
                    page = self.menu_pages[index][path]
                    page_html = menu_html
                    for key in page:
                        page_html = page_html.replace('{{%s}}' % key, str(page[key]))
                    site['menu[%d]' % index] += page_html
