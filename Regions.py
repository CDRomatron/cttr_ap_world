from .Locations import CTTRLocation, location_table

# (Region name, list of exits)
cttr_regions = [
    ('Midway',['Go to Mystery Island','Go to Happily Ever Faster','Go to Tyrannosaurus Wrecks', 'Go to Tomb Town', 'Go to Astro Land'])
]

mandatory_connections = [
    ('Go to Mystery Island', 'Mystery Island'),
    ('Go to Happily Ever Faster', 'Happily Ever Faster'),
    ('Go to Tyrannosaurus Wrecks', 'Tyrannosaurus Wrecks'),
    ('Go to Tomb Town', 'Tomb Town'),
    ('Go to Astro Land', 'Astro Land')
]

default_connections = {

}

illegal_connections = {
    
}