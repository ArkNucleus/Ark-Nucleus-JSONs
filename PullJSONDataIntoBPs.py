import json
import unreal


def change_blueprint_default_value(blueprint_generated_class, variable_name, new_value):
    blueprint = unreal.load_object(None, blueprint_generated_class)
    some_actor_cdo = unreal.get_default_object(blueprint)
    some_actor_cdo.set_editor_property(variable_name, new_value)

# LANGUAGES
with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-Localization\\languages.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/CoreBPs/Libraries/Nucleus_BaseSharedData.Nucleus_BaseSharedData_C", "Languages", json.dumps(jsonData))


# SHARED CCA LOCALIZATION
with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\shared-cca\\localization-example.json","r") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/SharedBPs/ArkNucleus_CCA_Base.ArkNucleus_CCA_Base_C", "MyMod_LocalizationStrings", json.dumps(jsonData))


# NUCLEUS CCA LOCALIZATION
with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-Localization\\nucleus-cca\\localization.json","r") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/CoreBPs/CCA/Ark-Nucleus_CCA.Ark-Nucleus_CCA_C", "MyMod_LocalizationStrings", json.dumps(jsonData))

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-Localization\\nucleus-cca\\server-localization.json","r") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/CoreBPs/CCA/Ark-Nucleus_CCA.Ark-Nucleus_CCA_C", "Nucleus_ServerLocalization_Default", json.dumps(jsonData))

# NUCLEUS CCA MOD INFO UI
with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\nucleus-cca\\mod-ui\\nuclues-info-ui.json","r") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/CoreBPs/CCA/Ark-Nucleus_CCA.Ark-Nucleus_CCA_C", "MyMod_CustomInfoUI", json.dumps(jsonData))

# NUCLEUS CCA SERVER INFO UI
with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\nucleus-cca\\main-page\\default-server-info-page.json","r") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/CoreBPs/CCA/Ark-Nucleus_CCA.Ark-Nucleus_CCA_C", "Nucleus_DefaultServerInfoPage", json.dumps(jsonData))

# NUCLEUS CCA UI CONFIGS
with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\nucleus-cca\\main-page\\main-page.json","r") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/CoreBPs/CCA/Ark-Nucleus_CCA.Ark-Nucleus_CCA_C", "Nucleus_MainUI", json.dumps(jsonData))

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\nucleus-cca\\main-page\\main-page-server-info.json","r") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/CoreBPs/CCA/Ark-Nucleus_CCA.Ark-Nucleus_CCA_C", "Nucleus_MainUI_ServerInfo", json.dumps(jsonData))

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\nucleus-cca\\main-page\\main-page-installed-mods.json","r") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/CoreBPs/CCA/Ark-Nucleus_CCA.Ark-Nucleus_CCA_C", "Nucleus_MainUI_InstalledMods", json.dumps(jsonData))

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\nucleus-cca\\main-page\\main-page-encyclopedia.json","r") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/CoreBPs/CCA/Ark-Nucleus_CCA.Ark-Nucleus_CCA_C", "Nucleus_MainUI_Encyclopedia", json.dumps(jsonData))

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\nucleus-cca\\main-page\\main-page-all-logs.json","r") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/CoreBPs/CCA/Ark-Nucleus_CCA.Ark-Nucleus_CCA_C", "Nucleus_MainUI_AllLogs", json.dumps(jsonData))

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\nucleus-cca\\main-page\\main-page-server-localization.json","r") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/CoreBPs/CCA/Ark-Nucleus_CCA.Ark-Nucleus_CCA_C", "Nucleus_MainUI_AllLocalizations", json.dumps(jsonData))

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\nucleus-cca\\main-page\\main-page-all-survivors.json","r") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/CoreBPs/CCA/Ark-Nucleus_CCA.Ark-Nucleus_CCA_C", "Nucleus_MainUI_AllSurvivors", json.dumps(jsonData))


# NUCLEUS CCA CLIENT SETTINGS
client_setting = {}
with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\nucleus-cca\\settings\\client-settings-localization.json","r") as jsonFile:
    jsonData = json.load(jsonFile)
    client_setting["LOCALIZATION"] = json.dumps(jsonData)

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\nucleus-cca\\settings\\client-settings-uihacks.json","r") as jsonFile:
    jsonData = json.load(jsonFile)
    client_setting["UIHACKS"] = json.dumps(jsonData)

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\nucleus-cca\\settings\\client-settings-colors.json","r") as jsonFile:
    jsonData = json.load(jsonFile)
    client_setting["COLORS"] = json.dumps(jsonData)



change_blueprint_default_value("/Ark-Nucleus/CoreBPs/CCA/Ark-Nucleus_CCA.Ark-Nucleus_CCA_C", "MyMod_DefaultClientSettings", client_setting)


# NUCLEUS CCA SERVER SETTINGS
server_setting = {}
with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\nucleus-cca\\settings\\server-settings-permissions.json","r") as jsonFile:
    jsonData = json.load(jsonFile)
    server_setting["PERMISSIONS"] = json.dumps(jsonData)

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\nucleus-cca\\settings\\server-settings-localization.json","r") as jsonFile:
    jsonData = json.load(jsonFile)
    server_setting["LOCALIZATION"] = json.dumps(jsonData)

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\nucleus-cca\\settings\\server-settings-encyclopedia.json","r") as jsonFile:
    jsonData = json.load(jsonFile)
    server_setting["ENCYCLOPEDIA"] = json.dumps(jsonData)

change_blueprint_default_value("/Ark-Nucleus/CoreBPs/CCA/Ark-Nucleus_CCA.Ark-Nucleus_CCA_C", "MyMod_DefaultServerSettings", server_setting)


# NUCLEUS CCA PLAYER SERVER SETTINGS
player_setting = {}
with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\nucleus-cca\\settings\\player-settings-general.json","r") as jsonFile:
    jsonData = json.load(jsonFile)
    player_setting["GENERAL"] = json.dumps(jsonData)

change_blueprint_default_value("/Ark-Nucleus/CoreBPs/CCA/Ark-Nucleus_CCA.Ark-Nucleus_CCA_C", "MyMod_DefaultPlayerServerSettings", player_setting)


# WIDGETS
# with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\widgets\\message-modal.json","r") as jsonFile:
#     jsonData = json.load(jsonFile)
#     change_blueprint_default_value("/Ark-Nucleus/DynamicUI/Widgets/DU_BaseWidget_v1.DU_BaseWidget_v1_C", "Nucleus_MessageModalUIConfig", json.dumps(jsonData))

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\widgets\\du-edit-color.json","r") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/DynamicUI/Widgets/Edit/DU_Edit_Color_v1.DU_Edit_Color_v1_C", "N_EditColor_ColorPickerUIConfig", json.dumps(jsonData))


with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\widgets\\du-edit-magic-category.json","r") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/DynamicUI/Widgets/Edit/DU_Edit_Magic_v1.DU_Edit_Magic_v1_C", "Nucleus_Edit_Category_UI", json.dumps(jsonData))

edit_widgets = {}
with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\widgets\\du-edit-magic-string.json","r") as jsonFile:
    jsonData = json.load(jsonFile)
    edit_widgets["STRING"] = json.dumps(jsonData)

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\widgets\\du-edit-magic-boolean.json","r") as jsonFile:
    jsonData = json.load(jsonFile)
    edit_widgets["BOOLEAN"] = json.dumps(jsonData)

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\widgets\\du-edit-magic-int.json","r") as jsonFile:
    jsonData = json.load(jsonFile)
    edit_widgets["INT"] = json.dumps(jsonData)

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\widgets\\du-edit-magic-array-string.json","r") as jsonFile:
    jsonData = json.load(jsonFile)
    edit_widgets["ARRAY-STRING"] = json.dumps(jsonData)

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\widgets\\du-edit-magic-array-object.json","r") as jsonFile:
    jsonData = json.load(jsonFile)
    edit_widgets["ARRAY-OBJECT"] = json.dumps(jsonData)

change_blueprint_default_value("/Ark-Nucleus/DynamicUI/Widgets/Edit/DU_Edit_Magic_v1.DU_Edit_Magic_v1_C", "Nucleus_Edit_Widgets", edit_widgets)


# PRE-BUILD
with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\widgets\\pre-build\\mod_info.json","r") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/DynamicUI/Widgets/PreBuiltComps/DU_PreBuilt_ModInfo_v1.DU_PreBuilt_ModInfo_v1_C", "N_BaseWidget_StaticUIConfig", json.dumps(jsonData))

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\widgets\\pre-build\\spawn.json","r") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/DynamicUI/Widgets/PreBuiltComps/DU_PreBuilt_Spawn_v1.DU_PreBuilt_Spawn_v1_C", "N_BaseWidget_StaticUIConfig", json.dumps(jsonData))

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\widgets\\pre-build\\advanced3d_view.json","r") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/DynamicUI/Widgets/PreBuiltComps/DU_PreBuilt_Advanced3DView_v1.DU_PreBuilt_Advanced3DView_v1_C", "N_BaseWidget_StaticUIConfig", json.dumps(jsonData))

print("SCRIPT DONE!")