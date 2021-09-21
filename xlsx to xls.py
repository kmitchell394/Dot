from win32com.client import Dispatch

xl = Dispatch('Excel.Application')
wb = xl.Workbooks.Add(r"\\server-md3\shared documents\Crystal Reports\Keith\Dot.xlsx")
wb.SaveAs(r"\\server-md3\shared documents\Crystal Reports\Keith\Dot33.xlss"[:-1], FileFormat=56)
xl.Quit()