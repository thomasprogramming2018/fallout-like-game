import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))

list_position = (50, 50)
list_size = (200, 400)
list_font = pygame.font.SysFont('fallouty', 24)
list_item_height = 30
box_position = (40, 40)
box_size = (120, 400)
box_color = (255, 255, 255)
box_thickness = 2
clickable_rects = []


def render_list(items, scroll_offset):
    pygame.draw.rect(screen, box_color, (*box_position, *box_size), box_thickness)

      # New list to store clickable regions

    start_index = max(0, scroll_offset // list_item_height)
    end_index = min(len(items), (scroll_offset + box_size[1]) // list_item_height + 1)

    for i, item in enumerate(items):
        item_y = list_position[1] + (i * list_item_height) - scroll_offset
        item_position = (list_position[0], item_y)

        # Create a rectangle for each item
        item_rect = pygame.Surface((list_size[0], list_item_height))
        #item_rect.clip_ip(pygame.Rect(*box_position, *box_size))
        item_rect = item_rect.get_rect()

        # Move the item rect to the correct position
        item_rect.move_ip(*item_position)
        #item_rect.fill((0, 0, 0))
        #clip_area = pygame.Rect(*box_position, *box_size)
        #item_rect.set_clip(clip_area)

        # Render the item text onto the screen
        item_text = list_font.render(items[i], True, (255, 255, 255))
        screen.blit(item_text, item_position)
        screen.blit(screen, item_position)
        # Store the clickable region (rectangle and item) in clickable_rects
        clickable_rects.append((item_rect.get_rect().move(item_position), items[i]))
        

    return clickable_rects
def main():
    items = ['i','i','i','i','g','l','i','i','i','i','i','i','i','i','i','i','i','i']
    scroll_offset = 0
    clicked = False
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
              # Check for mouse button press
            if event.type == MOUSEBUTTONDOWN and clicked == False:  # Check for mouse button press and cooldown
                mouse_pos = pygame.mouse.get_pos()
                for rect, item in clickable_rects:
                    if rect.collidepoint(mouse_pos):
                        clicked = True
                        print(f"Clicked item: {item}")
                        break
            if event.type == MOUSEBUTTONUP and clicked == True:
                clicked = False
        max_scroll_offset = max(0, len(items) * list_item_height - box_size[1])
        scroll_offset = min(max_scroll_offset, scroll_offset)
        # Handle scrolling
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            if scroll_offset > 0:
                scroll_offset -= 1
        elif keys[K_DOWN]:
            scroll_offset += 1
        

        # Render the list
        screen.fill((0, 0, 0))
        render_list(items, scroll_offset)
        pygame.display.flip()

if __name__ == '__main__':
    main()
