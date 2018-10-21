import os
from django.http import HttpResponse, Http404, StreamingHttpResponse, FileResponse

# Create your views here.
# Case 1: simple file download, very bad
# Reason 1: loading file to memory and consuming memory
# Can download all files, including raw python .py codes


def file_download(request, file_path):
    # do something...
    with open(file_path) as f:
        c = f.read()
    return HttpResponse(c)


# Case 2 Use HttpResponse to download a small file
# Good for txt, not suitable for big binary files
def media_file_download(request, file_path):
    with open(file_path, 'rb') as f:
        try:
            response = HttpResponse(f)
            response['content_type'] = "application/octet-stream"
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
        except Exception:
            raise Http404


# Case 3 Use StreamingHttpResponse to download a large file
# Good for streaming large binary files, ie. CSV files
# Do not support python file "with" handle. Consumes response time
def stream_http_download(request, file_path):
    try:
        response = StreamingHttpResponse(open(file_path, 'rb'))
        response['content_type'] = "application/octet-stream"
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
        return response
    except Exception:
        raise Http404


# Case 4 Use FileResponse to download a large file
# It streams the file out in small chunks
# It is a subclass of StreamingHttpResponse
# Use @login_required to limit download to logined users
def file_response_download1(request, file_path):
    try:
        response = FileResponse(open(file_path, 'rb'))
        response['content_type'] = "application/octet-stream"
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
        return response
    except Exception:
        raise Http404


# Case 5 Limit file download type - recommended
def file_response_download(request, file_path):
    ext = os.path.basename(file_path).split('.')[-1].lower()
    # cannot be used to download py, db and sqlite3 files.
    if ext not in ['py', 'db',  'sqlite3']:
        response = FileResponse(open(file_path, 'rb'))
        response['content_type'] = "application/octet-stream"
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
        return response
    else:
        raise Http404

