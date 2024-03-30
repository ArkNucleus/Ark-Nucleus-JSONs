import json
import unreal


def change_blueprint_default_value(blueprint_generated_class, variable_name, new_value):
    blueprint = unreal.load_object(None, blueprint_generated_class)
    some_actor_cdo = unreal.get_default_object(blueprint)
    some_actor_cdo.set_editor_property(variable_name, new_value)

# LANGUAGES
with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-Localization\\languages.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/SharedContent/Widgets/Edit/DU_Edit_LanguageDropDown_v1.DU_Edit_LanguageDropDown_v1_C", "N_EditLangDrop_SupportedLanguages", json.dumps(jsonData))

# SHARED CCA LOCALIZATION
with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\shared-cca\\localization-example.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/BaseContent/ArkNucleus_CCA_Base.ArkNucleus_CCA_Base_C", "MyMod_LocalizationStrings", json.dumps(jsonData))

############################################
#                BASIC CCA                 #
############################################

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\nucleus-cca-basic\\main-page\\main-page.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/SharedContent/Ark-Nucleus_CCA_Basic.Ark-Nucleus_CCA_Basic_C", "N_Basic_MainUI", json.dumps(jsonData))

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\nucleus-cca-basic\\main-page\\main-page-json-playground.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/SharedContent/Ark-Nucleus_CCA_Basic.Ark-Nucleus_CCA_Basic_C", "N_Basic_MainUI_JsonPlayground", json.dumps(jsonData))

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\nucleus-cca-basic\\main-page\\default-json-playground.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/SharedContent/Ark-Nucleus_CCA_Basic.Ark-Nucleus_CCA_Basic_C", "N_Basic_JsonPlayground_Default", json.dumps(jsonData))

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\nucleus-cca-basic\\main-page\\main-page-encyclopedia.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/SharedContent/Ark-Nucleus_CCA_Basic.Ark-Nucleus_CCA_Basic_C", "N_Basic_MainUI_Encyclopedia", json.dumps(jsonData))

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\nucleus-cca-basic\\main-page\\main-page-installed-mods.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/SharedContent/Ark-Nucleus_CCA_Basic.Ark-Nucleus_CCA_Basic_C", "N_Basic_MainUI_InstalledMods", json.dumps(jsonData))

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\nucleus-cca-basic\\main-page\\main-page-all-logs.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/SharedContent/Ark-Nucleus_CCA_Basic.Ark-Nucleus_CCA_Basic_C", "N_Basic_MainUI_AllLogs", json.dumps(jsonData))
    
    
with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\nucleus-cca-basic\\mod-ui\\no-mod-custom-info.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/SharedContent/Ark-Nucleus_CCA_Basic.Ark-Nucleus_CCA_Basic_C", "N_Basic_Mods_NoCustomInfoPage", json.dumps(jsonData))
    
with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\nucleus-cca-basic\\mod-ui\\nucleus-info-ui.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/SharedContent/Ark-Nucleus_CCA_Basic.Ark-Nucleus_CCA_Basic_C", "MyMod_CustomInfoUI", json.dumps(jsonData))

############################################
#                MAIN CCA                  #
############################################

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\nucleus-cca\\main-page\\main-page.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/PrivateContent/Ark-Nucleus_CCA.Ark-Nucleus_CCA_C", "N_Basic_MainUI", json.dumps(jsonData))

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\nucleus-cca\\main-page\\main-page-server-info.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/PrivateContent/Ark-Nucleus_CCA.Ark-Nucleus_CCA_C", "Nucleus_MainUI_ServerInfo", json.dumps(jsonData))

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\nucleus-cca\\main-page\\main-page-server-localization.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/PrivateContent/Ark-Nucleus_CCA.Ark-Nucleus_CCA_C", "Nucleus_MainUI_AllLocalizations", json.dumps(jsonData))

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\nucleus-cca\\main-page\\main-page-all-survivors.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/PrivateContent/Ark-Nucleus_CCA.Ark-Nucleus_CCA_C", "Nucleus_MainUI_AllSurvivors", json.dumps(jsonData))


with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\nucleus-cca\\main-page\\default-server-info-page.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/PrivateContent/Ark-Nucleus_CCA.Ark-Nucleus_CCA_C", "Nucleus_DefaultServerInfoPage", json.dumps(jsonData))

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\nucleus-cca\\main-page\\disabled-server-info-page.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/PrivateContent/Ark-Nucleus_CCA.Ark-Nucleus_CCA_C", "Nucleus_DisabledServerInfoPage", json.dumps(jsonData))


with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\widgets\\struct-painter-uihack.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/PrivateContent/Ark-Nucleus_CCA.Ark-Nucleus_CCA_C", "Nucleus_StructPainter_UIConfig", json.dumps(jsonData))

############################################
#              LOCALIZATION                #
############################################

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-Localization\\nucleus-cca\\localization.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/SharedContent/Ark-Nucleus_CCA_Basic.Ark-Nucleus_CCA_Basic_C", "MyMod_LocalizationStrings", json.dumps(jsonData))

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-Localization\\nucleus-cca\\server-localization.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/PrivateContent/Ark-Nucleus_CCA.Ark-Nucleus_CCA_C", "Nucleus_ServerLocalization_Default", json.dumps(jsonData))


with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\temp.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/SharedContent/Ark-Nucleus_CCA_Basic.Ark-Nucleus_CCA_Basic_C", "N_Basic_Mods_FakeCFData", json.dumps(jsonData))

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\temp.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/PrivateContent/Ark-Nucleus_CCA.Ark-Nucleus_CCA_C", "N_Basic_Mods_FakeCFData", json.dumps(jsonData))


############################################
#                 SETTINGS                 #
############################################

# NUCLEUS CCA CLIENT SETTINGS
client_setting = {}
with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\nucleus-cca-basic\\settings\\client-settings-uihacks.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    client_setting["UIHACKS"] = json.dumps(jsonData)

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\nucleus-cca-basic\\settings\\client-settings-colors.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    client_setting["COLORS"] = json.dumps(jsonData)



change_blueprint_default_value("/Ark-Nucleus/SharedContent/Ark-Nucleus_CCA_Basic.Ark-Nucleus_CCA_Basic_C", "MyMod_DefaultClientSettings", client_setting)


# NUCLEUS CCA SERVER SETTINGS

server_setting = {}

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\nucleus-cca-basic\\settings\\server-settings-general.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    server_setting["GENERAL"] = json.dumps(jsonData)

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\nucleus-cca-basic\\settings\\server-settings-api.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    server_setting["API"] = json.dumps(jsonData)

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\nucleus-cca-basic\\settings\\server-settings-localization.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    server_setting["LOCALIZATION"] = json.dumps(jsonData)

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\nucleus-cca-basic\\settings\\server-settings-permissions.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    server_setting["PERMISSIONS"] = json.dumps(jsonData)

change_blueprint_default_value("/Ark-Nucleus/SharedContent/Ark-Nucleus_CCA_Basic.Ark-Nucleus_CCA_Basic_C", "MyMod_DefaultServerSettings", server_setting)


# NUCLEUS CCA PLAYER SERVER SETTINGS
player_setting = {}
with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\nucleus-cca-basic\\settings\\player-settings-general.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    player_setting["GENERAL"] = json.dumps(jsonData)

change_blueprint_default_value("/Ark-Nucleus/SharedContent/Ark-Nucleus_CCA_Basic.Ark-Nucleus_CCA_Basic_C", "MyMod_DefaultPlayerServerSettings", player_setting)


with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\widgets\\du-edit-color.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/SharedContent/Widgets/Edit/DU_Edit_Color_v1.DU_Edit_Color_v1_C", "N_EditColor_ColorPickerUIConfig", json.dumps(jsonData))


with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\widgets\\du-edit-magic-category.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/SharedContent/Widgets/Edit/DU_Edit_Magic_v1.DU_Edit_Magic_v1_C", "Nucleus_Edit_Category_UI", json.dumps(jsonData))

edit_widgets = {}

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\widgets\\du-edit-magic-object.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    edit_widgets["OBJECT"] = json.dumps(jsonData)

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\widgets\\du-edit-magic-string.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    edit_widgets["STRING"] = json.dumps(jsonData)

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\widgets\\du-edit-magic-boolean.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    edit_widgets["BOOLEAN"] = json.dumps(jsonData)

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\widgets\\du-edit-magic-int.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    edit_widgets["INT"] = json.dumps(jsonData)

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\widgets\\du-edit-magic-array-string.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    edit_widgets["ARRAY-STRING"] = json.dumps(jsonData)

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\widgets\\du-edit-magic-array-object.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    edit_widgets["ARRAY-OBJECT"] = json.dumps(jsonData)

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\widgets\\du-edit-magic-array-player.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    edit_widgets["ARRAY-PLAYER"] = json.dumps(jsonData)

change_blueprint_default_value("/Ark-Nucleus/SharedContent/Widgets/Edit/DU_Edit_Magic_v1.DU_Edit_Magic_v1_C", "Nucleus_Edit_Widgets", edit_widgets)


# PRE-BUILD
with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\widgets\\pre-build\\mod_info.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/SharedContent/Widgets/PreBuiltComps/DU_PreBuilt_ModInfo_v1.DU_PreBuilt_ModInfo_v1_C", "N_BaseWidget_StaticUIConfig", json.dumps(jsonData))

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\widgets\\pre-build\\item_info.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/SharedContent/Widgets/PreBuiltComps/DU_PreBuilt_ItemInfo_v1.DU_PreBuilt_ItemInfo_v1_C", "N_BaseWidget_StaticUIConfig", json.dumps(jsonData))

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\widgets\\pre-build\\spawn.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/SharedContent/Widgets/PreBuiltComps/DU_PreBuilt_Spawn_v1.DU_PreBuilt_Spawn_v1_C", "N_BaseWidget_StaticUIConfig", json.dumps(jsonData))

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\widgets\\pre-build\\struct_painter.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/PrivateContent/Widgets/Nucleus_W_Misc_SlotButtons.Nucleus_W_Misc_SlotButtons_C", "N_BaseWidget_StaticUIConfig", json.dumps(jsonData))

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\widgets\\pre-build\\advanced3d_view.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/SharedContent/Widgets/PreBuiltComps/DU_PreBuilt_Advanced3DView_v1.DU_PreBuilt_Advanced3DView_v1_C", "N_BaseWidget_StaticUIConfig", json.dumps(jsonData))
    
with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\widgets\\item-modal.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/SharedContent/Widgets/ListItems/DU_Item_PrimalItemDino_v2.DU_Item_PrimalItemDino_v2_C", "DU_Item_ModalUIConfig", json.dumps(jsonData))

# BASE WIDGET
with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\widgets\\base-widget\\du_base-basic-error.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/SharedContent/Widgets/DU_BaseWidget_v1.DU_BaseWidget_v1_C", "N_BaseWidget_CONST_ErrorWidget", json.dumps(jsonData))

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\widgets\\base-widget\\du_base-basic-modal.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/SharedContent/Widgets/DU_BaseWidget_v1.DU_BaseWidget_v1_C", "N_BaseWidget_CONST_Modal", json.dumps(jsonData))

with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\widgets\\base-widget\\du_base-basic-notif.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/SharedContent/Widgets/DU_BaseWidget_v1.DU_BaseWidget_v1_C", "N_BaseWidget_CONST_NotifWidget", json.dumps(jsonData))

# TABBED PANEL
with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\widgets\\du-panel-tabbed.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/SharedContent/Widgets/Panels/DU_Panel_Tabbed_v1.DU_Panel_Tabbed_v1_C", "Nucleus_CONST_TabButtonUIConfig", json.dumps(jsonData))


with open("G:\\GitRepos\\ArkModding\\Ark-Nucleus-JSONs\\widgets\\du-edit-dropdown-default-item.json","r", encoding="utf8") as jsonFile:
    jsonData = json.load(jsonFile)
    change_blueprint_default_value("/Ark-Nucleus/SharedContent/Widgets/Edit/DU_Edit_DropDown_v1.DU_Edit_DropDown_v1_C", "N_DropDown_DefaultItemWidget", json.dumps(jsonData))

print("SCRIPT DONE!")