# -*- coding: utf-8 -*-

import arcpy
from datetime import datetime
import os


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [LayerCloner]


class LayerCloner(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Layer Cloner"
        self.description = "Clone one or more layers with the current date suffix"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter(
            displayName="Select Features to Clone:",
            name="in_features",
            multiValue=True,
            datatype=["GPFeatureLayer"],
            parameterType="Required",
        )
        param1 = arcpy.Parameter(
            displayName="Cloned Output Name:",
            name="out_features",
            multiValue=True,
            datatype="String",
            enabled=False,
        )
        param2 = arcpy.Parameter(
            displayName="Geodatabase Output Location (Workspace)",
            name="in_workspace",
            datatype="DEWorkspace",
            enabled=True,
            direction="Input",
            parameterType="Required"
        )
        param2.defaultEnvironmentName = "Workspace"

        params = [param0, param1, param2]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        cur_date = datetime.now().strftime("%Y%m%d")
        if parameters[0].values:
            layer_names = []
            for p in parameters[0].values:
                layer_names.append(p.name + "_" + cur_date)

            layer_names_str = ";".join(layer_names)
            parameters[1].value = layer_names_str

            parameters[1].enabled = True
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        wkspc = parameters[2].valueAsText
        arcpy.AddMessage(f"Workspace: {wkspc}")

        #Export copies of selected Features
        inFeatures = parameters[0].values
        outNames = parameters[1].values

        for index, item in enumerate(inFeatures):
            arcpy.AddMessage(f'Index: {index}, Feature: {item.name}, Data Source: {item.dataSource}')
            outPath = os.path.join(wkspc, outNames[index])
            arcpy.AddMessage(f'Output Path: {outPath}')
            
            if item.dataSource.lower()[-4:] == ".shp":
                arcpy.AddMessage("Feature is a shapefile")
                arcpy.conversion.FeatureClassToFeatureClass(item.dataSource, wkspc, outNames[index])
            else:
                arcpy.AddMessage("Feature Layer detected")
                arcpy.management.Copy(item.dataSource, outPath)            

        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
