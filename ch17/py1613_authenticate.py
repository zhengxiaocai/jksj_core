# >>TODO: 身份认证
import functools


def authenticate(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        request = args[0]
        if check_user_logged_in(request):
            func(*args, **kwargs)
        else:
            raise Exception('Authentication Failed')

    return wrapper


def check_user_logged_in(*args):
    return True


@authenticate
def post_comment(requst, *args):
    print('发表成功')


if __name__ == '__main__':
    post_comment(1)
