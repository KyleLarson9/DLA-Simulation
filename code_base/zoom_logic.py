import pygame as pg

class Zoom_Logic:

    def zoom(mouse_x, mouse_y, vis, event):
        # mouse position before zoom
        mouse_grid_col = mouse_x / (vis.TILE_SIZE * vis.zoom) + vis.top_left_col
        mouse_grid_row = mouse_y / (vis.TILE_SIZE * vis.zoom) + vis.top_left_row

        # zoom in or out
        if event.y > 0:
            vis.zoom *= 1.1
        elif event.y < 0:
            vis.zoom *= .9

        vis.zoom = max(vis.min_zoom, min(vis.zoom, vis.max_zoom)) # cap zoom to min and max 

        # mouse positoin after zoom
        mouse_grid_col_zoomed = mouse_x / (vis.TILE_SIZE * vis.zoom) + vis.top_left_col
        mouse_grid_row_zoomed = mouse_y / (vis.TILE_SIZE * vis.zoom) + vis.top_left_row

        # shift camera
        vis.top_left_col += mouse_grid_col - mouse_grid_col_zoomed
        vis.top_left_row += mouse_grid_row - mouse_grid_row_zoomed
    
    def pan(keys, vis):
        if keys[pg.K_a] or keys[pg.K_LEFT]:
            vis.top_left_col -= vis.speed
        if keys[pg.K_d] or keys[pg.K_RIGHT]:
            vis.top_left_col += vis.speed
        if keys[pg.K_w] or keys[pg.K_UP]:
            vis.top_left_row -= vis.speed
        if keys[pg.K_s] or keys[pg.K_DOWN]:
            vis.top_left_row += vis.speed

    def drag_camera(vis, mouse_x, mouse_y):
        # mouse drag: move camera
        dx = mouse_x - vis.drag_start_mouse[0]
        dy = mouse_y - vis.drag_start_mouse[1]

        # convert pixel movement to grid movement
        vis.top_left_col = vis.drag_start_cam[0] - dx / (vis.TILE_SIZE * vis.zoom)
        vis.top_left_row = vis.drag_start_cam[1] - dy / (vis.TILE_SIZE * vis.zoom)