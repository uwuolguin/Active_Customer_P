import tableauserverclient as TSC

tableau_auth = TSC.PersonalAccessTokenAuth('uwu96', '', 'bulls')
server = TSC.Server('https://10ax.online.tableau.com/', use_server_version=True)
server.auth.sign_in(tableau_auth)

workbook = server.workbooks.get_by_id('')
print(workbook.id)

server.workbooks.populate_views(workbook)
print([(view.name, view.id) for view in workbook.views])