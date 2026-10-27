def markdown_to_blocks(markdown: str) -> list[str]:
    potential_blocks = markdown.split("\n\n")
    blocks = []
    for potential_block in potential_blocks:
        new_block = potential_block.strip()
        if new_block == "":
            continue
        blocks.append(new_block)
    return blocks