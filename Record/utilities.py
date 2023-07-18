# from django.http import HttpResponse
# from openpyxl import load_workbook
# from pr1 import write_pr1

# def convert_excel_to_pr1(request):
#     excel_file = request.FILES['excel_file']
#     wb = load_workbook(excel_file)
#     pr1_data = write_pr1(wb)
#     with open('pr1_file.pr1', 'wb') as f:
#         f.write(pr1_data)
#     return HttpResponse('File converted successfully.')
