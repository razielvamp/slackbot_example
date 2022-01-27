from message import Message


def run_action(message: Message) -> str:

    if message.text == 'info':
        return f'Your ID is {message.user} and you sent [{message.text}] command'

    if message.text == 'disk usage':
        import shutil
        stat = shutil.disk_usage('/')
        return f'Disk total size is {stat.total} bytes and {stat.used} bytes used'

    return 'unknown command'
