from st_pages import Page, show_pages, add_page_title

# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages(
    [
        Page("Pages/app.py", "Dashboard"),
        Page("Pages/cluster.py", "Segmentation Report"),
    ]
)
